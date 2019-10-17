from kafka import KafkaProducer
from schemas import serialize, get_schema, create_headers_for_schema
from config import bootstrap_address, topicname, apikey, cert, es_restapi
from config import schemaid, schemaversion, test_message

# Create a Kafka client ready to produce messages
producer = KafkaProducer(bootstrap_servers=bootstrap_address,
                         security_protocol="SASL_SSL",
                         ssl_cafile=cert,
                         ssl_check_hostname=False,
                         sasl_plain_username="token",
                         sasl_plain_password=apikey,
                         sasl_mechanism="PLAIN",
                         client_id="python-producer-dale")

# Get the schema to use to serialize the message
schema = get_schema(schemaid, schemaversion, es_restapi, apikey, cert)

# message key if needed
key = None

# Send the serialized message to the Kafka topic
producer.send(topicname,
              serialize(schema, test_message),
              key,
              create_headers_for_schema(schemaid, schemaversion))
producer.flush()
