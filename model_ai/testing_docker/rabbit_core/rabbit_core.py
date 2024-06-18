from rabbitmq import RabbitMQ_comms

rabbit2 = RabbitMQ_comms()

while(True):
    rabbit2.send_message("Hello world")