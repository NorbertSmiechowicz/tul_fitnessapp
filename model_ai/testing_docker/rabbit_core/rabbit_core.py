from rabbitmq import RabbitMQ_comms
from pymongo import MongoClient

rabbit2 = RabbitMQ_comms()

# Connect to MongoDB server
client = MongoClient('mongo', 27017)

# Access the database
db = client.mydatabase
# Access the collection
collection = db.mycollection
# Fetch all records
records = collection.find()
# Print each record
for record in records:
    rabbit2.send_message(record)