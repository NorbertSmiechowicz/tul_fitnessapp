import pika
from pika.exchange_type import ExchangeType

"""
Publisher Script:

    Connection: Establish a connection to the RabbitMQ server using pika.ConnectionParameters.
    Channel: Open a channel through which communication will take place.
    Queue Declaration: Ensure the queue named 'hello' exists.
    Publish Message: Use basic_publish to send a message to the queue.
    Close Connection: Close the connection once the message is sent.
Consumer Script:

    Connection: Similar to the publisher, establish a connection to the RabbitMQ server.
    Channel: Open a channel.
    Queue Declaration: Ensure the queue named 'hello' exists.
    Callback Function: Define a callback function that will process messages from the queue.
    Start Consuming: Use basic_consume to subscribe to the queue and start consuming messages. The callback function is called whenever a message is received.

"""

class RabbitMQ_comms:
    def __init__(self) -> None:
        self.credentials = pika.PlainCredentials('your_username', 'your_password')
        self.parameters = pika.ConnectionParameters('localhost', 5672, '/', self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def send_message(self, message):
        self.channel.exchange_declare(exchange='FoodApp', exchange_type=ExchangeType.fanout)
        self.channel.basic_publish(exchange='FoodApp', routing_key='', body=message)
        print(f"sent message: {message}")
        self.connection.close()

    def receive_message(self):
        def on_message_received(ch, method, properties, body):
            print(f"firstconsumer: received new message: {body}")
            self.connection.close()

        self.channel.exchange_declare(exchange='FoodApp', exchange_type=ExchangeType.fanout)

        queue = self.channel.queue_declare(queue='', exclusive=True)

        self.channel.queue_bind(exchange='FoodApp', queue=queue.method.queue)

        self.channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

        print("Starting Consuming")

        self.channel.start_consuming()

        print("*********************")