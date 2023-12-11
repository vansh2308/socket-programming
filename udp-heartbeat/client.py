from socket import *
import time

server_host = "127.0.0.1"
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
seq = 1

while True:
  client_socket.sendto(f"Ping {seq} {time.time()}".encode(), (server_host, server_port))
  seq += 1
  time.sleep(2)
