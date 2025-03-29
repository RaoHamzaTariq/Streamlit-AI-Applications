import socket
import pickle
import threading
from player import Player
import random

class Server:
    def __init__(self, host='192.168.2.127', port=5555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(5)
        self.players = {}
        self.next_id = 0
        self.lock = threading.Lock()
        print(f"Server started on {host}:{port}")
        
    def handle_client(self, conn, player_id):
        """Handle communication with a client"""
        # Send the player's ID first
        conn.send(pickle.dumps(player_id))
        
        try:
            while True:
                # Receive player data
                data = pickle.loads(conn.recv(2048))
                if not data:
                    break
                    
                # Update player position
                with self.lock:
                    self.players[player_id] = data
                    
                # Send back all players' data
                conn.send(pickle.dumps(self.players))
                
        except:
            # Client disconnected
            pass
        finally:
            # Remove player and close connection
            with self.lock:
                if player_id in self.players:
                    del self.players[player_id]
            conn.close()
            print(f"Player {player_id} disconnected")
            
    def run(self):
        """Accept connections and start client threads"""
        print("Waiting for connections...")
        try:
            while True:
                conn, addr = self.server.accept()
                print(f"Connected to: {addr}")
                
                # Create a new player at random position
                with self.lock:
                    player_id = self.next_id
                    self.next_id += 1
                    
                    x = random.randint(50, 750)
                    y = random.randint(50, 550)
                    player = Player(player_id, x, y)
                    self.players[player_id] = player
                
                # Start thread to handle this client
                thread = threading.Thread(target=self.handle_client, args=(conn, player_id))
                thread.daemon = True
                thread.start()
                
        except KeyboardInterrupt:
            print("Server shutting down")
        finally:
            self.server.close()

# Start the server when script is run directly
if __name__ == "__main__":
    server = Server()
    server.run()