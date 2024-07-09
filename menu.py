import json
import getpass
from redisdb import iniciar_sessao, verificar_sessao, temporario_usuario, limpar_temporario_usuario, obter_temporario_usuario, conectRedis
from mongodb import cadastrar_usuario, verificar_credenciais, usuario

def criar_conta_temporaria():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = getpass.getpass("Senha: ")
    temporario_usuario(nome, email, senha)
    print("Usuário temporário criado com sucesso.")

def registrar_usuario_definitivo():
    email = input("Email do usuário temporário: ")
    temp_user = obter_temporario_usuario(email)
    if temp_user:
        nome = input("Nome: ")
        cadastrar_usuario(nome, temp_user['senha'], email)
        limpar_temporario_usuario(email)
        print("Usuário registrado com sucesso.")
    else:
        print("Usuário temporário não encontrado.")

def menu_login():
    print("Bem-vindo ao Mercado Livre :)")
    while True:
        escolha = input("Escolha uma opção:\n  1. Login\n  2. Criar conta temporária\n  3. Registrar conta definitiva\n  4. Sair\nOpção: ")
        if escolha == '1':
            email = input("Email: ")
            senha = getpass.getpass("Senha: ")

            user = verificar_credenciais(email, senha)
            if user:
                token = iniciar_sessao(email)
                print(f"Login bem-sucedido! Token da sessão: {token}")
                
                menu2 = input("O que deseja fazer agora?\n 1. Alterar dados usuário \nOpção:")
                if menu2 == '1':
                    tempDefinitiva = input("Conta temporário (T) ou definitiva (D)? ").upper()
                    if tempDefinitiva == "T":
                        usuarioAlterar = usuario.find_one({"email": email})
                        if usuarioAlterar:
                            usuarioJson = json.dumps(usuarioAlterar, default=str)
                            nomeNovo = input("Digite o novo nome: ")
                            
                            if nomeNovo: usuarioJson['nome'] = nomeNovo
                            
                            usuario.update_one({"_id": usuarioJson["email"]}, {"$set": usuarioJson})
                            print("Usuário alterado no Mongo com sucesso!")


                        else:
                            print("Usuário logado não encontrado no Mongo")
                    else:
                        usuarioAlterar = conectRedis.get(email)
                        if usuarioAlterar:
                            usuarioJson = json.dumps(usuarioAlterar, default=str)
                            nomeNovo = input("Digite o novo nome: ")
                            
                            if nomeNovo: usuarioJson['nome'] = nomeNovo
                            
                            conectRedis.set(email, usuarioJson)
                            print("Usuário alterado no Redis com sucesso!")
                        else:
                            print("Usuário logado não encotrado no Redis")

            else:
                print("Credenciais inválidas.")
        
        elif escolha == '2':
            criar_conta_temporaria()

        elif escolha == '3':
            registrar_usuario_definitivo()

        elif escolha == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_login()