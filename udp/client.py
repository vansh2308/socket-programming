from socket import *

server_name = "localhost"
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)


while(True):
  message =input("Enter lowercase string: ")
  client_socket.sendto(message.encode(), (server_name, server_port))
  modified_msg, server_addr = client_socket.recvfrom(2048)
  print(modified_msg.decode())

  option = input("Do you want to continue (y/n)? ")
  if(option.lower() == "n"):
    client_socket.close()
    break

client_socket.close()



