from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
# AF_INET is the connection family for ipv4 

server_socket.bind(("", server_port))
# empty string for all ipv4 connections 
# "127.0.0.1" only for loopback connections 

server_socket.listen(1)
print("The server is ready to recieve: ")

while True:
  connection_socket, addr = server_socket.accept()
  print(connection_socket, addr)
  sentence = connection_socket.recv(1024).decode()
  connection_socket.send(sentence.upper().encode())
  connection_socket.close()
  
server_socket.close()

