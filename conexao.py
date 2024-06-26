import redis
import pymongo
from pymongo.server_api import ServerApi
 
# Conexão com o Redis
conectRedis = redis.Redis(
    host='redis-13985.c281.us-east-1-2.ec2.redns.redis-cloud.com',
    port=13985,
    password='djKSLT6YdkSykmDTFUqSGabMZEeNCoNb'
)
 
# Conexão com o MongoDB
uri = 'mongodb+srv://marianasilva155:marianasilva155@fatecnosql.vyamlgr.mongodb.net/?retryWrites=true&w=majority&appName=FatecNoSQL'
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
db = client.MercadoLivre
collection = db["Usuário"]