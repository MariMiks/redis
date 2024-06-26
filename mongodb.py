import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb+srv://marianasilva155:marianasilva155@fatecnosql.vyamlgr.mongodb.net/?retryWrites=true&w=majority&appName=FatecNoSQL'
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
db = client.MercadoLivre
collection = db["Usuário"]

def cadastrar_usuario(nome, senha, email):
    usuarios.insert_one({'nome': nome, 'senha': senha, 'email': email})

def verificar_credenciais(email, senha):
    usuario = usuarios.find_one({'email': email, 'senha': senha})
    return usuario
