import pygame
from network import Network
from game import Game
from player import Player
import sys

# Initialize pygame
pygame.init()

# Game settings
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Multiplayer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS
FPS = 60

def main():
    """Main client function"""
    # Get server address
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = 'localhost'  # Default server address
    
    # Connect to server
    print(f"Connecting to server at {host}...")
    network = Network(host, 5555)
    player_id = network.connect()
    
    if player_id is None:
        print("Could not connect to server")
        return
        
    print(f"Connected as Player {player_id}")
    
    # Create local player and game
    local_player = Player(player_id)
    game = Game(WIDTH, HEIGHT)
    
    # Game loop variables
    clock = pygame.time.Clock()
    running = True
    
    # Main game loop
    while running:
        clock.tick(FPS)
        
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        # Process key presses for movement
        keys = pygame.key.get_pressed()
        local_player.move(keys, WIDTH, HEIGHT)
        
        # Send player data to server and get all players
        players = network.send(local_player)
        if players:
            game.update_players(players)
        
        # Draw everything
        game.draw(WIN, player_id)
        pygame.display.update()
    
    # Cleanup
    pygame.quit()

if __name__ == "__main__":
    main()