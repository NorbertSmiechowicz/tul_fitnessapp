from rabbitmq import RabbitMQ_comms
import logging
import logstash
import sys
from rabbitmq import RabbitMQ_comms
from pymongo import MongoClient

# Konfiguracja logowania
logstash_host = 'logstash'
logstash_port = 5044

logger = logging.getLogger('rabbit_ai')
logger.setLevel(logging.INFO)
logstash_handler = logstash.TCPLogstashHandler(logstash_host, logstash_port, version=1)
logger.addHandler(logstash_handler)

# Możliwość logowania również do konsoli
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

rabbit1 = RabbitMQ_comms()

def on_message_received(ch, method, properties, body):
    logger.info(f"firstconsumer: received new message: {body}")

while(True):
    rabbit1.receive_message(on_message_received=on_message_received)