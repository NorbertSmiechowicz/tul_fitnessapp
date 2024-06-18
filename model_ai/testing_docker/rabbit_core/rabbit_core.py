"""
from rabbitmq import RabbitMQ_comms
from pymongo import MongoClient

client = MongoClient('mongodb')
db = client["mydatabase"]
collection = db["mycollection"]

myquery = { "name": { "$regex": "^." } }

mydoc = collection.find(myquery)

msg_list = []

for record in mydoc:
    msg_list.append(f"imie : {record['name']}")

rabbit2 = RabbitMQ_comms()

while(1):
    for record in msg_list:
        rabbit2.send_message(record)
        

        

# client = MongoClient("mongodb://localhost:27017/")
# db = client["mydatabase"]
# collection = db["mycollection"]

# myquery = { "name": { "$regex": "^." } }

# mydoc = collection.find(myquery)

# for record in mydoc:
#     print(record['name'])
#     print(type(record))

"""

import logging
import logstash
import sys
from rabbitmq import RabbitMQ_comms
from pymongo import MongoClient

# Konfiguracja logowania
logstash_host = 'logstash'
logstash_port = 5044

logger = logging.getLogger('rabbit_core')
logger.setLevel(logging.INFO)
logstash_handler = logstash.TCPLogstashHandler(logstash_host, logstash_port, version=1)
logger.addHandler(logstash_handler)

# Możliwość logowania również do konsoli
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

# Połączenie z MongoDB
client = MongoClient('mongodb')
db = client["mydatabase"]
collection = db["mycollection"]

# Wyszukiwanie w kolekcji MongoDB
myquery = { "name": { "$regex": "^." } }
mydoc = collection.find(myquery)

msg_list = []
for record in mydoc:
    msg_list.append(f"imie : {record['name']}")
    # Logowanie każdego rekordu
    logger.info(f"Fetched record from MongoDB: {record}")

# Inicjalizacja RabbitMQ
rabbit2 = RabbitMQ_comms()

# Pętla wysyłająca wiadomości
while True:
    for record in msg_list:
        rabbit2.send_message(record)
        logger.info(f"Sent message to RabbitMQ: {record}")



