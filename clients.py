
import pygame
from Clients.network import Network

width = 500
height = 500

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Clients")

clientNum = 0

class Player():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win,self.color,self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

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
        self.rect = (self.x,self.y,self.width,self.height)

def read_pos(str):# "45,65" convert to (45,65)
    str = str.split(",")
    return int(str[0]), int(str[1])

def read_pos2(str):# "45,65" convert to (45,65)
    str = str.split(",")
    return int(str[0]), int(str[1]), int(str[2]), int(str[3])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def covert(tp):
    return str(tp[0])+","+str(tp[1]),str(tp[2])+","+str(tp[3])

def redrawWindow(win,player,player2,player3):
    win.fill((255,255,255,255))
    player.draw(win)
    player2.draw(win)
    player3.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos()) # server Connected and received
    # main() # this part is the sending enemy player date to player
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,255,0))
    p3 = Player(2,2,100,100,(0,0,255))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        recv = n.send(make_pos((p.x, p.y)))
        m = make_pos((12,20))
        # main() # this def&part is the receiving enemy player data and convert the str to int (ex: "(100,10,34,55)" -> 100,10,34,55 )
        m2 = read_pos2(recv)
        print("V2",m)
        print("V23",m2[0],m2[1],m2[2],m2[3],)
        print("vecter :"+str((p.x,p.y)))
        #print(p2Pos[0],p2Pos[1])

        # main() # this part is the setting enemy player position,dress,life of received data
        # enemy red
        p2.x = m2[0]
        p2.y = m2[1]
        p2.update()
        #  enemy blue
        p3.x = m2[2]
        p3.y = m2[3]
        p3.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p,p2,p3)
main()

