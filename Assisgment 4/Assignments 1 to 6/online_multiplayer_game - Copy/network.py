import socket
import pickle

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "192.168.2.127"
        self.port = 5555
        self.addr = (self.server,self.port)
        self.id = self.connect()
        self.p = self.connect()

    def getP(self):
        return self.ppos
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048).decode())
        except:
            pass

    def send(self,data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))


n = Network()