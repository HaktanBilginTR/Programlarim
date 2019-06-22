import pygame

import random


pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("oyun")
clock = pygame.time.Clock()
point = 0
death = 0

class bullet():

    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.height = 15
        self.width = 15
        self.color = (0,0,255)
        self.vel = 10
        self.rect = (self.x, self.y, self.height, self.width)

    def move(self):

        self.x += self.vel
        self.rect = (self.x, self.y, self.height, self.width)

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)

    def son(self):
        if self.x >= 600:
            del self
            global xd, b
            xd = False
            b = bullet(p.x, p.y + p.height/3)


class enemy():

    def __init__(self, height = 40, width = 40, color = (0,255,0)):
        self.x = 600
        self.y = self.y_gen()
        self.height = height
        self.width = width
        self.color = color
        self.vel = 3.5
        self.rect = (self.x, self.y, self.height, self.width)

    def move(self):
        self.x -= self.vel
        self.draw()

        if self.collide():
            self.x = 600
            self.y = self.y_gen()
            global point
            point += 1

        if self.x <= 0:
            self.x = 600
            self.y = self.y_gen()
            global death
            death += 1

        self.rect = (self.x, self.y, self.height, self.width)

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)

    def y_gen(self):
        num = random.randrange(0, 550)
        return num

    def collide(self):

        if self.x + self.width >= b.x >= self.x and self.y + self.height >= b.y >= self.y:
            return True
        elif self.x + self.width >= b.x + b.width >= self.x and self.y + self.height >= b.y >= self.y:
            return True
        elif self.x + self.width >= b.x >= self.x and self.y + self.height >= b.y + b.height >= self.y:
            return True
        elif self.x + self.width >= b.x + b.width >= self.x and self.y + self.height >= b.y + b.height >= self.y:
            return True


class sprite():

    def __init__(self, x, y, height, width, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.vel = 5
        self.rect = (self.x, self.y, self.height, self.width)

    def move(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        self.rect = (self.x, self.y, self.height, self.width)

    def draw(self):

        pygame.draw.rect(win, self.color, self.rect)

    def fire(self):

        b.move()


def redrawWindow(x):
    x.draw()

    pygame.display.flip()


Game = True
xd = False
p = sprite(50, 300, 45, 45)
b = bullet(p.x, p.y+ p.height/3)
e1 = enemy()
e2 = enemy()
e3 = enemy()

font = pygame.font.SysFont("ComicSansMs", 42)
text = font.render(str(death), True, (0, 128, 0))
win.blit(text, (545 - text.get_width() // 2, 55 - text.get_height() // 2))

while Game:
    clock.tick(60)
    win.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:

                b.x = p.x
                b.y = p.y
                xd = True
                b = bullet(p.x, p.y + p.height/3)

    if xd:
        b.move()
        b.draw()
    p.move()
    e1.move()
    e2.move()
    e3.move()

    if p.x <= 0:
        p.x = 0.1
    if p.x >= 90:
        p.x = 89.9
    if p.y <= 0:
        p.y = 0.1
    if p.y >= 555:
        p.y = 554

    if death >= 10:
        pygame.quit()
        print(point)

    redrawWindow(p)
    b.son()


