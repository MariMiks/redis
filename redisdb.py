import redis
import json
import uuid

conectRedis = redis.Redis(
    host='redis-14966.c99.us-east-1-4.ec2.redns.redis-cloud.com:14966',
    port=13985,
    password='8Oa3FMcHvk69FYtVJcS3xJsk32se6X49'
)

def iniciar_sessao(email):
    token = str(uuid.uuid4())
    conectRedis.set(token, email)
    conectRedis.expire(token, 1800) # 30min * 60

def verificar_sessao(token):
    if conectRedis.exists(token):
        conectRedis.expire(token, 1800)
        return conectRedis.get(token).decode('utf-8')
    return None

def temporario_usuario(nome, email, senha):
    chave = f"temp_user:{email}"
    dados_usuario = json.dumps({'nome': nome, 'email': email, 'senha': senha})
    conectRedis.set(chave, dados_usuario)
    conectRedis.expire(chave, 600) # 10min * 60

def obter_temporario_usuario(email):
    chave = f"temp_user:{email}"
    dados_usuario = conectRedis.get(chave)
    if dados_usuario:
        return json.loads(dados_usuario.decode('utf-8'))
    return None

def limpar_temporario_usuario(email):
    chave = f"temp_user:{email}"
    conectRedis.delete(chave)
