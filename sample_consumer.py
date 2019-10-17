import json
from kafka import KafkaConsumer
from schemas import deserialize, get_schema_from_message
from config import bootstrap_address, topicname, apikey, cert, es_restapi

# Create a Kafka client ready to consume messages
consumer = KafkaConsumer(topicname,
                         bootstrap_servers=bootstrap_address,
                         security_protocol="SASL_SSL",
                         ssl_cafile=cert,
                         ssl_check_hostname=False,
                         sasl_plain_username="token",
                         sasl_plain_password=apikey,
                         sasl_mechanism="PLAIN",
                         client_id="python-consumer-dale")

# for each message received from the topic...
for msg in consumer:
    # get the schema to use for this message
    schema = get_schema_from_message(msg, es_restapi, apikey, cert)

    if schema:
        # deserialize the message value using the
        # schema identified in the message headers
        data = deserialize(schema, msg.value)
    else:
        data = msg.value

    # print the received message
    print (json.dumps(data))
