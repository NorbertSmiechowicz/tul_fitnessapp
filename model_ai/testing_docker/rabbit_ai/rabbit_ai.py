from rabbitmq import RabbitMQ_comms

rabbit1 = RabbitMQ_comms()

while(True):
    rabbit1.receive_message()