class Player:
    def __init__(self, id, x=100, y=100):
        self.id = id
        self.x = x
        self.y = y
        self.color = (255, 0, 0)  # Default color is red
        self.size = 30
        self.speed = 5
        
    def move(self, keys, width, height):
        """Handle player movement based on key presses"""
        import pygame
        if keys[pygame.K_LEFT]:
            self.x = max(self.x - self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.x = min(self.x + self.speed, width - self.size)
        if keys[pygame.K_UP]:
            self.y = max(self.y - self.speed, 0)
        if keys[pygame.K_DOWN]:
            self.y = min(self.y + self.speed, height - self.size)
    
    def draw(self, window):
        """Draw the player on the window"""
        import pygame
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
        
        # Draw player ID
        font = pygame.font.SysFont("arial", 20)
        text = font.render(f"P{self.id}", 1, (0, 0, 0))
        window.blit(text, (self.x + 10, self.y - 20))