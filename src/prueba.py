import socket               # Import socket module
import _thread
from mqtt import AwsMqtt
def on_new_client(clientsocket,addr,mqttclient):
    while True:
        data = clientsocket.recv(1024)
        if data:
            print(data)
            data = str(data).split(',')
            if data[0] == "b'+RESP:GTSOS":
                payload = {
                    "mensaje": "MSJ: Papi te amo",
                    "url": "Estoy aqui: "+"https://www.google.com/maps/search/?api=1&query="+data[12]+","+data[11]
                }
                if data[2] == "869912030003251":
                    payload["nombre"] = "Nicolas"
                if data[2] == "015181000143272":
                    payload["nombre"] = "Isaac"
                mqttclient.subscribe(topic="sos")
                mqttclient.publish(topic="sos", payload=payload)

    clientsocket.close()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 29800                # Reserve a port for your service.

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
mqttclient = AwsMqtt(endpointurl="a2qr6sez1bqltp-ats.iot.us-east-1.amazonaws.com",endpointport=8883)

while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   _thread.start_new_thread(on_new_client,(c,addr,mqttclient))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()