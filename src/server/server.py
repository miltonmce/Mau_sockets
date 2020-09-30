import socket
import json
import os
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address given on the command line
server_address = (socket.gethostname(), 29800)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(5)
countsos = 0


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
payload2 = {"msj": "te quiero papa ven por mi", "url": "url google map"}
myMQTTClient.subscribe("/helloworld", 1, helloworld)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(128)
            # print('{!r}'.format(data))
            if data:
                data = str(data).split(',')
                if data[0] == "b'+BUFF:GTFRI":
                    print(data)
                    myMQTTClient.publish("/helloworld", str(payload2), 0)
                    pass

                    # print("https://www.google.com/maps/search/?api=1&query="+data[12]+","+data[11])
                if data[0] == "b'+RESP:GTSOS":
                    contador += 1
                    print(contador)
                    print(
                        "ayudaaameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee quiero una nieveeee")
                    print(
                        "https://www.google.com/maps/search/?api=1&query="+data[12]+","+data[11])

                # connection.sendall(data)
            else:
                break
    finally:
        connection.close()


class ServerSocket(object):

    def __init__(self, sock=None):
        super().__init__()
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.host = (socket.gethostname(), 29800)
        self.countsos = 0
        self.status = 0

    def connect(self, host, port):
        self.sock.connect((host, port))

    def connection(self, connection):
        try:
            data = connection.recv(128)
            if data:
                data = str(data).split(',')
                if data[0] == "b'+RESP:GTFRI":
                    payload = {"status": self.status, "msg": "", "url": ""}
                    if self.status == 0:
                        print(type(json.dump(payload)))
                    self.status = 1

                if data[0] == "b'+RESP:GTSOS":
                    self.countsos += 1
                    payload = {"status": self.status, "msg": "ven por mi papi estoy aqui",
                               "url": "https://www.google.com/maps/search/?api=1&query=" + data[12] + "," + data[11]}
                    print(json.dumps(payload))
                    self.status = 0
            else:
                return False
        finally:
            connection.close()

    def runserver(self):
        self.sock.bind(self.host)
        self.sock.listen(5)  # listen 5 connections
        while True:
            connection, client_address = self.sock.accept()
            validate = self.connection(connection)
            if validate == False:
                break

        pass
