import os
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


def _subscrib(self, params, packet):
    print('Received meessage from AWS IoT Core')
    print('Topic: ' + packet.topic)
    print('payload:', (packet.payload))

class AwsMqtt():

    def __init__(self,endpointurl:str,endpointport:int):
        self.endpointurl = endpointurl
        self.endpointport = endpointport
        self.pem = os.path.join( "private", "AmazonRootCA1.pem")
        self.key = os.path.join( "private", "private.pem.key")
        self.crt = os.path.join( "private", "certificate.pem.crt")
        self.client = AWSIoTMQTTClient("JMPV_clientid")
        self._config()
        self.client.connect()

    def _config(self):
        self.client.configureEndpoint(self.endpointurl, self.endpointport)
        # Set path for Root CA and unique device credentials (use the private key and certificate retrieved from the logs in Step 1)
        self.client.configureCredentials(self.pem, self.key, self.crt)
        self.client.configureOfflinePublishQueueing(-1)
        self.client.configureDrainingFrequency(2)
        self.client.configureConnectDisconnectTimeout(10)
        self.client.configureMQTTOperationTimeout(5)



    def subscribe(self,topic:str):
        self.client.subscribe(topic,1,_subscrib)

    def publish(self,topic:str,payload:dict):
        self.client.publish(topic,json.dumps(payload),1)
