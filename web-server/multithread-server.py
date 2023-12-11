from socket import *
import _thread

server_socket = socket(AF_INET, SOCK_STREAM)
server_port = 12000
server_socket.bind(('', server_port))
server_socket.listen(1)

def serve_request(connection_socket: socket):
  # print(_thread.get_native_id())
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

print(f"Server listening at port {server_port}")
while True:
  connection_socket, addr = server_socket.accept()
  _thread.start_new_thread(serve_request, (connection_socket, ))

server_socket.close()

  
