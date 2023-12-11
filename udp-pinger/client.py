from socket import *
import datetime
import time

client_socket = socket(AF_INET, SOCK_DGRAM)
server_port = 12000
server_host = "127.0.0.1"

rtt_list = []

print("\n")
for i in range(10):
  start = time.perf_counter()
  client_socket.sendto(f"Ping {i+1} {datetime.datetime.now()}".encode(), (server_host, server_port))

  try:
    client_socket.settimeout(1)
    response = client_socket.recv(1024)
    end = time.perf_counter()
    rtt = end-start
    rtt_list.append(rtt)
    print(response.decode() + f"\t {rtt}")
    client_socket.settimeout(None)
  
  except timeout: 
    print(f"Ping {i+1} {datetime.datetime.now()} \t Request Timed out")

print("\n")
print(f"Max rtt: {max(rtt_list)}")
print(f"Min rtt: {min(rtt_list)}")
print(f"Avg rtt: {sum(rtt_list)/float(len(rtt_list))}")
print(f"Package loss %: {(10-len(rtt_list))*10}")




