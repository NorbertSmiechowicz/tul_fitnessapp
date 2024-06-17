import elasticapm
from elasticapm.handlers.logging import LoggingHandler
import logging

apm_client = elasticapm.Client({
    'SERVICE_NAME': 'your-service-name',
    'SECRET_TOKEN': 'your-secret-token',
    'SERVER_URL': 'http://localhost:8200',
})

logger = logging.getLogger('python-elastic-apm-logger')
logger.setLevel(logging.INFO)
apm_handler = LoggingHandler(client=apm_client)
logger.addHandler(apm_handler)