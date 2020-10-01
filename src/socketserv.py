import socket
from mqtt import AwsMqtt


class SocketServer:
    def __init__(self, port: int, endpointurl: str, endpointport: int):
        """
        :param port: integer port
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = port
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.mqttclient = AwsMqtt(endpointurl, endpointport)

    def runserver(self):
        print('waiting for a connection')
        connection, client_address = self.sock.accept()
        try:
            print('client connected:', client_address)
            while True:
                data = connection.recv(128)
                if data:
                    data = str(data).split(',')
                    if data[0] == "b'+RESP:GTSOS":
                        print(data)
                        self.mqttclient.subscribe(topic="sos")
                        self.mqttclient.publish(topic="sos", payload=data)
                    # connection.sendall(data)
                else:
                    break
        except Exception as e:
            print("client disconected")
        finally:
            connection.close()
