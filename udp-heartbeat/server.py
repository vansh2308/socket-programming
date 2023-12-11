from socket import *
import time

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("", 12000))
seq = 1
while True:
  server_socket.settimeout(10/2)
  try:
    msg, addr = server_socket.recvfrom(1024)
  except timeout:
    print("The client is closed!")
    server_socket.close()
    break

  server_socket.settimeout(None)
  msg = msg.decode().split(" ")
  print(f"seq: {msg[1]} \t time_diff: {time.time()-float(msg[2])}")
  print(f"Packets lost: {int(msg[1])-seq}")
  seq+=1

