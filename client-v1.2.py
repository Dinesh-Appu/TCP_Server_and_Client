import socket

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 2409
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server Started")
server_socket.connect((IP,PORT))
print("Server connected")

def recive():
 byt = server_socket.recv(1240)
 print(byt)
 stri = input("Please Type Message : ")
 meg = bytes(stri,'utf-8')
 server_socket.send(meg)
 return stri


if __name__ == '__main__':
    recive()
    server_socket.close()

