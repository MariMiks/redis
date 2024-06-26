from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['sistema_login']
usuarios = db.usuarios

def cadastrar_usuario(nome, senha):
    usuarios.insert_one({'nome': nome, 'senha': senha})

def verificar_credenciais(nome, senha):
    usuario = usuarios.find_one({'nome': nome, 'senha': senha})
    return usuario
