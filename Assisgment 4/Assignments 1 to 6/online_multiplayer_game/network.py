import socket
import pickle

class Network:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.id = None
        
    def connect(self):
        """Connect to server and get initial data"""
        try:
            self.client.connect(self.addr)
            self.id = pickle.loads(self.client.recv(2048))
            return self.id
        except:
            print("Connection failed")
            return None
            
    def send(self, data):
        """Send data to server and receive response"""
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(f"Error: {e}")
            return None