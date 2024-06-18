from rabbitmq import RabbitMQ_comms
from pymongo import MongoClient

rabbit2 = RabbitMQ_comms()
client = MongoClient('mongo', 27017)
db = client.mydatabase
collection = db.mycollection
records = collection.find()

for i, record in enumerate(records):
    print(record)
    rabbit2.send_message(f"Record [{i}] : {record}")

while(True):
    rabbit2.send_message("Test only str")