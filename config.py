# See the README.md for help in populating this.


# 1.
#
# Name of the topic to consume a message from
topicname="YOUR-TOPIC-NAME"


# 2.
#
# Bootstrap address for Kafka clients connecting to Event Streams
#
#  Find this on the "Connect to this topic" panel in the admin UI
#  or in the CLI output from `cloudctl es init`
bootstrap_address = "YOUR-HOST-NAME:PORT"


# 3.
#
# API key for connecting to Event Streams
#
#  Create this using the "Generate API Key" wizard in the admin UI
#  or using the CLI command `cloudctl es iam-service-id-create`
apikey = "YOUR-API-KEY"


# 4.
#
# Location of the certificate to use for connecting to Event Streams
#
#  Download this from the "Connect to this topic" panel in the admin UI
#  or using the CLI command `cloudctl es certificates --format pem`
cert="/your/cluster/certificate/es-cert.pem"


# 5.
#
# URL for the Event Streams Schema Registry REST API
#
#  Find this on the "Connect to this topic" panel in the admin UI
#  or in the CLI output from `cloudctl es init`
es_restapi = "https://YOUR-HOST-NAME:REST-PORT"


# 6.
#
# ID of the schema to use
schemaid="YOUR-SCHEMA-ID"
# Version of the schema to use
schemaversion="1"


# 7.
#
# A test message to send that has a format consistent with the
# schema referred to above.
test_message = {
    "SomeTestString" : "Hello World",
    "SomeTestNumber" : 123
}
