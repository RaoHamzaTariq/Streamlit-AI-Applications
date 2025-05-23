import socket
from _thread import *
import sys

server = "192.168.2.127"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)


s.listen(2)
print("Waiting for connection, Server Started")

players = [Player(0,0,50,50,(255,0,0)),Player(100,100,50,50,(0,255,0))]

def read_pos(str):
    str = str.split(",")
    return int(str[0],str[1])
        
def make_pos(tup):
    return str(tup[0]+","+tup[1])

pos = [(0,0),(100,100)]

def threaded_client(conn,player):
    conn.send(pickle.loads(players[player]))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode("utf-8"))
            pos[player] = data


            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Recieved: ",data)
                print("Sending: ",reply)
            
            conn.sendall(pickle.dumps(reply))
        except Exception as e:
           break
    
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("connected to:", addr)

    start_new_thread(threaded_client,(conn,currentPlayer))
    currentPlayer+=1