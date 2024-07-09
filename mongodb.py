import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import bcrypt

uri = 'mongodb+srv://marianasilva155:marianasilva155@fatecnosql.vyamlgr.mongodb.net/?retryWrites=true&w=majority&appName=FatecNoSQL'
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
db = client.MercadoLivre
global usuario
usuario = db["Usuário"]

def cadastrar_usuario(nome, senha, email):
    senhaCripto = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    usuario.insert_one({'nome': nome, 'senha': senhaCripto, 'email': email})

def verificar_credenciais(email, senha):
    user = usuario.find_one({'email': email, 'senha': senha})
    if user and bcrypt.checkpw(senha.encode('utf-8'), user['senha']):
        return user
    return None
