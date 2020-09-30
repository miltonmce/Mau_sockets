import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import os
import json


def helloworld(self, params, packet):
    print('Received meessage from AWS IoT Core')
    print('Topic: ' + packet.topic)
    print('payload:', (packet.payload))


# path certificate
pem = os.path.join("src", "private", "AmazonRootCA1.pem")
key = os.path.join("src", "private", "private.pem.key")
crt = os.path.join("src", "private", "certificate.pem.crt")
print(pem)


# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("JMPV_clientid")
# For TLS mutual authentication
# Provide your AWS IoT Core endpoint (Example: "abcdef12345-ats.iot.us-east-1.amazonaws.com")
myMQTTClient.configureEndpoint(
    "a2qr6sez1bqltp-ats.iot.us-east-1.amazonaws.com", 8883)
# Set path for Root CA and unique device credentials (use the private key and certificate retrieved from the logs in Step 1)
myMQTTClient.configureCredentials(pem, key, crt)
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)

print("Connecting...")
myMQTTClient.connect()
payload2 = {"status": "1", "msj": "te quiero papa ven por mi",
            }
myMQTTClient.subscribe("milton", 1, helloworld)
myMQTTClient.publish("milton", str(payload2), 0)
payload2 = {"status": "0", "": "te quiero papa ven por mi",
            }
myMQTTClient.publish("milton", str(payload2), 0)


while True:
    time.sleep(5)
