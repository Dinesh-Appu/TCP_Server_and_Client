
import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.43.213"
        self.port = 3262
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
             self.client.connect(self.addr)
             l = self.client.recv(4999).decode()
             print("connect & received: "+l)
             return l
        except:
            pass

    def send(self, data):
        try:
            s = self.client.send(str.encode(data))
            l = self.client.recv(4999).decode()  # 45,0,65,0
            print("Sended : "+str(s))
            print("Received : "+l)
            return l
        except socket.error as e:
            print(e)




