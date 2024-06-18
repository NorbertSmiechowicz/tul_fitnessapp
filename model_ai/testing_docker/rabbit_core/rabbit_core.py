from rabbitmq import RabbitMQ_comms

rabbit2 = RabbitMQ_comms()

rabbit2.send_message("Hello world")