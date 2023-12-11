from socket import *
import random

serverSocket = socket(AF_INET, SOCK_DGRAM)
server_port =12000
serverSocket.bind(("", server_port))
print(f"Server listening at port: {server_port}")

while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    # print(message.decode())
    if rand < 4:
        continue
    serverSocket.sendto(message, address)