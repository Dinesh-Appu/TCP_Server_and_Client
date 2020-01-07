import socket
import select

HEADER_LENGTH = 1024
IP = "127.0.0.1"
PORT = 2409
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server Started")
server_socket.bind((IP,PORT))
server_socket.listen()
print("Waiting for connection...")
sockets_list = [server_socket]
clients = {}

conn, addr = server_socket.accept()
print("Client connected : "+addr)

def resive_message():
        conn.send(b"Hi am server")
        message_header = conn.recv(HEADER_LENGTH)
        meg = str(message_header,'utf-8')
        print(meg)
        return message_header

if __name__ == '__main__':
    resive_message()
    server_socket.close()

