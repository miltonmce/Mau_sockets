from socketserv import SocketServer


if __name__ == '__main__':
    sock = SocketServer(port=29800,endpointurl="a2qr6sez1bqltp-ats.iot.us-east-1.amazonaws.com",endpointport=8883)
    while True:
        sock.runserver()


    pass