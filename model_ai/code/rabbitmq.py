import pika

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

def send_message_rabbit(message):
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # Declare a queue
    channel.queue_declare(queue='hello')
    # Send a message
    channel.basic_publish(exchange='',
                        routing_key='from_MODULE_AI',
                        body=message)
    connection.close()

def receive_message_rabbit():
    message_received = 0 
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue (make sure the queue exists)
    channel.queue_declare(queue='hello')

    # Callback function to process received messages
    def callback(ch, method, properties, message_received):
        print(f" [x] Received {message_received}")

    # Set up subscription on the queue
    channel.basic_consume(queue='hello',
                        on_message_callback=callback,
                        auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    return message_received

