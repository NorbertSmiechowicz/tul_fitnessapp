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


#Viewing Logs in Kibana
#Open Kibana and navigate to the Discover tab.
#Select the appropriate index pattern (e.g., python-logs-* for logs sent via Logstash).
#You should see your logged messages there, and you can use Kibana's powerful features to search, filter, and visualize the logs.