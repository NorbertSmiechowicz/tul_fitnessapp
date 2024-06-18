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