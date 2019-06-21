
import pygame
pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("game")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        #self.rect = (x, y, width, height)
        self.vel = 3
        self.image_sag = pygame.image.load("adam_sag.png")
        self.image_sol = pygame.image.load("adam_sol.png")
        self.image_yukari = pygame.image.load("adam_yukari.png")
        self.image_assagi = pygame.image.load("adam_assagi.png")
        self.image = self.image_sag
        self.rect = self.image.get_rect()

    #def draw(self, win):
    #    pygame.draw.rect(win, self.color, self.rect)

    def blit(self, win):
        win.blit(self.image, (self.x, self.y))


    def move1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.image = self.image_sol

        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.image = self.image_sag

        if keys[pygame.K_DOWN]:
            self.y += self.vel
            self.image = self.image_assagi

        if keys[pygame.K_UP]:
            self.y -= self.vel
            self.image = self.image_yukari

        """self.rect = (self.x, self.y, self.width, self.height)"""





def redrawWindow(win, player):

    player.blit(win)
    pygame.display.flip()


def main():
    gameLoop = True
    clock = pygame.time.Clock()
    p1 = Player(height/2, width/2, 50, 50, (255, 0, 0))


    while gameLoop:
        clock.tick(60)
        win.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False


        p1.move1()
        redrawWindow(win, p1)
















main()


exit()





