import pygame

class Game:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.players = {}  # Dictionary of players
        
    def update_players(self, players_data):
        """Update all players from server data"""
        self.players = players_data
        
    def draw(self, window, player_id):
        """Draw the game state"""
        window.fill((255, 255, 255))  # White background
        
        # Draw grid lines
        for i in range(0, self.width, 50):
            pygame.draw.line(window, (200, 200, 200), (i, 0), (i, self.height))
        for i in range(0, self.height, 50):
            pygame.draw.line(window, (200, 200, 200), (0, i), (self.width, i))
            
        # Draw players
        for id, player in self.players.items():
            # Assign different colors to each player
            if id == player_id:
                player.color = (255, 0, 0)  # Red for current player
            else:
                player.color = (0, 0, 255)  # Blue for other players
                
            player.draw(window)
            
        # Draw player count
        font = pygame.font.SysFont("arial", 25)
        text = font.render(f"Players: {len(self.players)}", 1, (0, 0, 0))
        window.blit(text, (10, 10))