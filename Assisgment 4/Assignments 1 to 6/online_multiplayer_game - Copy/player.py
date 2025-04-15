import sys
import pygame


class  Player():
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)

    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def move(self):
        pygame.keys.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            
        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
