import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='FoodApp', exchange_type=ExchangeType.fanout)

message = "This is a second producer"

channel.basic_publish(exchange='FoodApp', routing_key='', body=message)

print(f"sent message: {message}")

connection.close()