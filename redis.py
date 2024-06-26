import redis
import json

r = redis.Redis(
    host='redis-13985.c281.us-east-1-2.ec2.redns.redis-cloud.com',
    port=13985,
    password='djKSLT6YdkSykmDTFUqSGabMZEeNCoNb'
)


def temporario_usuario(nome, senha):
    chave = f"temp_user:{nome}"
    dados_usuario = json.dumps({'nome': nome, 'senha': senha})
    r.set(chave, dados_usuario)
    r.expire(chave, 600)  # Expira em 10 minutos (600 segundos)

def obter_temporario_usuario(nome):
    chave = f"temp_user:{nome}"
    dados_usuario = r.get(chave)
    if dados_usuario:
        return json.loads(dados_usuario.decode('utf-8'))
    return None

def limpar_temporario_usuario(nome):
    chave = f"temp_user:{nome}"
    r.delete(chave)
