from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", server_port))
server_socket.listen(1)


while True:
  print(f"Server listening at port: {server_port}")
  connection_socket, addr = server_socket.accept()
  msg = connection_socket.recv(1024)
  filename = msg.split()[1].decode()
  
  try:
    file = open(filename[1:], 'rb')
    file_content = file.read()
    connection_socket.send(b'''HTTP/1.1 200 OK\r\n\r\n''')
    connection_socket.send(file_content)
  except:
    file_content = open("./error.html", 'rb').read()
    connection_socket.send(b'''HTTP/1.1 404 Not Found\r\n\r\n''')
    connection_socket.send(file_content)

  connection_socket.close()

server_socket.close()


