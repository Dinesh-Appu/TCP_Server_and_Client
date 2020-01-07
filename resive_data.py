import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.1', 8040))
strl = 'I am CLIENT'
client.send(bytes(strl,'utf-8'))
from_server = client.recv(4096)
client.close()
print(from_server)