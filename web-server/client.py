import sys
from socket import *

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_host, server_port))

client_socket.send(f"GET /{filename} HTTP/1.1\r\nHost: {gethostbyname(gethostname())}:{str(client_socket.getsockname()[1])}\r\n\r\n".encode())

response = client_socket.recv(1024).decode()
print ("\n", response, end="\n\n")
fileData = client_socket.recv(10000)
print (fileData.decode())

client_socket.close()
