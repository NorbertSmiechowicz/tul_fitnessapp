import pika
from pika.exchange_type import ExchangeType
import time

class RabbitMQ_comms:
    def init(self) -> None:
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self.parameters = pika.ConnectionParameters('rabbit', 5672, '/', self.credentials)  # Use 'rabbit' as hostname (service name in Docker Compose)
        self.connection = None
        self.channel = None
        self.connect()

    def connect(self):
        attempts = 0
        while attempts < 3:
            try:
                self.connection = pika.BlockingConnection(self.parameters)
                self.channel = self.connection.channel()
                return
            except pika.exceptions.AMQPConnectionError as e:
                print(f"Failed to connect to RabbitMQ: {e}")
                attempts += 1
                time.sleep(5)  # Wait for 5 seconds before retrying

        raise RuntimeError("Failed to establish connection to RabbitMQ after multiple attempts")

    def send_message(self, message):
        self.channel.exchange_declare(exchange='FoodApp', exchange_type=ExchangeType.fanout)
        self.channel.basic_publish(exchange='FoodApp', routing_key='', body=message)
        print(f"sent message: {message}")

    def receive_message(self):
        def on_message_received(ch, method, properties, body):
            print(f"firstconsumer: received new message: {body}")

        self.channel.exchange_declare(exchange='FoodApp', exchange_type=ExchangeType.fanout)

        queue = self.channel.queue_declare(queue='', exclusive=True)

        self.channel.queue_bind(exchange='FoodApp', queue=queue.method.queue)

        self.channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

        print("Starting Consuming")

        self.channel.start_consuming()