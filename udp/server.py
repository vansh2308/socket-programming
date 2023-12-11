from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("", server_port))
print("The server is ready to recieve!")

while(True):
  message, client_addr =server_socket.recvfrom(2048)
  print(message, client_addr)

  server_socket.sendto(message.decode().upper().encode(), client_addr)




