from socket import *
import time
import base64
import ssl
import os
# from 
username = "agarwal.25@iitj.ac.in"
pwd = "pwd"
rec = "vanshagarwal11@gmail.com"
name = username.split("@")[0]
subject = "Hi dad"
msg = "Bans here!" 
endmsg = "\r\n.\r\n"
buf_size = 2048

# creating client socket 
mail_server = "smtp.gmail.com"
mail_server_port = 465
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.settimeout(5)

client_socket.connect((mail_server, mail_server_port))
context = ssl.create_default_context()
ssl_socket = context.wrap_socket(client_socket, server_hostname=mail_server)
# ssl_socket = ssl.wrap_socket(client_socket)
# ssl_socket.connect((mail_server, mail_server_port))
print(ssl_socket.recv(buf_size).decode())


def send_msg(msg:str, res:bool=True):
  ssl_socket.send(f"{msg}\r\n".encode())
  if res:
    try:
      print(ssl_socket.recv(buf_size).decode())
    except timeout:
      pass
  return

# # EHLO (for Extended SMTP) command and print server response.
send_msg("EHLO smtp.google.com")

# # auth login 
send_msg("AUTH LOGIN")
send_msg(base64.b64encode(username.encode()).decode())
send_msg(base64.b64encode(pwd.encode()).decode())

# # mail from, rcpt to, data 
send_msg(f"MAIL FROM:<{username}>")
send_msg(f"RCPT TO:<{rec}>")
send_msg(f"DATA")
send_msg(f"SUBJECT: {subject}\r\n", False)
send_msg(msg, False)
send_msg(".")


# # QUIT 
send_msg("QUIT")
