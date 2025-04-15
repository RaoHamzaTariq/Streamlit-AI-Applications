import pygame
from network import Network
# from player import Player
import pickle 
pygame.font.init()

width=500
height=500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, color, x,y, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = 150
        self.height = 150
        self.text = text

    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans",40)
        text = font.render(self.text,1,(255,255,255))
        win.blit(text,(self.x+round(self.width/2)-round(text.get_width()/2),self.y+round()))

    def click(self,pos):
        x1 = pos[0]
        y1 = pos[1]
        if x1 > self.x and x1 < self.x + self.width and y1 > self.y and y1 < self.y + self.height:
            return True
        else:
            return False




def redrawWindow(win,player,p):
    win.fill((255,255,255))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans",40)
        text = font.render("Waiting for player...",1,(0,0,0))
        win.blit(text,(width/2 - 150, height/2 - 25))
    else:
        font = pygame.font.SysFont("comicsans",40)
        text = font.render("Player 1: " + str(p),1,(0,0 ,0))
        win.blit(text,(10,10))
        
        text = font.render("Player 2: " + str(player),1,(0,0, 0))
        win.blit(text,(10,50))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        if game.bothWent():
            text1 = font.render(move1,1,(0,0,0))
            text2 = font.render(move2,1,(0,0,0))
        else:
            if game.p1Went() and p==0:
                text1 = font.render(move1,1,(0,0,0))
            elif game.p1Went():
                text1 = font.render("Locked In",1,(0,0,0))
            else:
                text1 = font.render("Waiting...",1,(0,0,0))

            if game.p2Went() and p==1:
                text2 = font.render(move2,1,(0,0,0))
            elif game.p2Went():
                text2 = font.render("Locked In",1,(0,0,0))
            else:
                text2 = font.render("Waiting...",1,(0,0,0))
            
            if p == 1:
                win.blit(text2,(10,90))
                win.blit(text1,(10,130))
            else:
                win.blit(text1,(10,90))
                win.blit(text2,(10,130))

            for btn in btns:
                btn.draw(win)

    
    pygame.display.update()

btns = [Button(
    100, 500, 100, 50, "Lock In", (0, 255, 0)
),
Button(
    300, 500, 100, 50, "Reset", (0, 0, 255)
),
Button(
    500, 500, 100, 50, "Quit", (255, 0, 0)
),
Button(
    700, 500, 100, 50, "Next Round", (0, 255, 255)
),
Button(
    900, 500, 100, 50, "Back to Menu", (255, 255, 0)
),
Button(
    1100, 500, 100, 50, "Play Again", (0, 0, 0)
)
]

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print( "Player's ID:", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print( "Couldn't get game.")
            break

        font = pygame.font.SysFont("comicsans",90)
        if (game.winner() ==1 and player==1) or (game.winner()==0 and player==0):
            text = font.render("You Win!", 1, (255,0,0))
        elif game.winner() == -1:
            text = font.render("Tie!", 1, (255,0,0))
        else:
            text = font.render("You Lose!", 1, (255,0,0))

        
        win.blit(text,(width/2- text.get_width()/2,height/2-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for btn in btns:
                if btn.click(pos) and game.connected():
                    if player ==0:
                        if not game.p1Went:
                            n.send(btn.text)
                    else:
                        if not game.p2Went:
                            n.send(btn.text)

    redrawWindow(win,game,player)


def menu_screen():
    run = True
    # n =Network()

    clock = pygame.time.Clock()
    win.fill((120,120,120))

    while run:
        clock.tick(60)
        font = pygame.font.SysFont("Arial", 30)
        text = font.render("Welcome to the game!",1,(0,0,0))
        win.blit(text,(10,10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    
    main()


while True:
    menu_screen()
