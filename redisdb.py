import redis
import json

r = redis.Redis(
    host='redis-13985.c281.us-east-1-2.ec2.redns.redis-cloud.com',
    port=13985,
    password='djKSLT6YdkSykmDTFUqSGabMZEeNCoNb'
)

def iniciar_sessao(nome):
    token = str(uuid.uuid4())
    r.set(token, nome)
    r.expire(token, 1800)  # Sessão expira em 30 minutos (1800 segundos)

def verificar_sessao(token):
    if r.exists(token):
        r.expire(token, 1800)  # Renova o tempo de expiração
        return r.get(token).decode('utf-8')
    return None

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
