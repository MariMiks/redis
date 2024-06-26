import getpass


def menu_login():
    print("Bem-vindo ao Mercado Livre :)")
    while True:
        escolha = input("Escolha uma opção:\n  1. Login\n  2. Criar conta\n  3. Sair\nOpção: ")
        if escolha == '1':
            nome = input("Nome de usuário: ")
            senha = getpass.getpass("Senha: ")

            if verificar_credenciais(nome, senha):
                token = iniciar_sessao(nome)
                print(f"Login bem-sucedido! Token da sessão: {token}")
            else:
                print("Credenciais inválidas.")
        
        elif escolha == '2':
            nome = input("Novo nome de usuário: ")
            senha = getpass.getpass("Nova senha: ")
            cadastrar_usuario(nome, senha)
            print("Usuário criado com sucesso.")

        elif escolha == '3':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_login()