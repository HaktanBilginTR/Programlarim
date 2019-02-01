import pygame

import random

import tkinter.messagebox


pygame.init()

gameDisplay = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
point = 0
bg = pygame.image.load("Bg.jpg")


def detect(x1, y1, w1, h1, x2, y2, w2, h2, x3, y3, w3, h3, x4, y4, w4, h4):
    if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2:
        return True
    elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2:
        return True
    elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
        return True
    elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
        return True

    if x3 + w3 >= x1 >= x3 and y3 + h3 >= y1 >= y3:
        return True
    elif x3 + w3 >= x1 + w1 >= x3 and y3 + h3 >= y1 >= y3:
        return True
    elif x3 + w3 >= x1 >= x3 and y3 + h3 >= y1 + h1 >= y3:
        return True
    elif x3 + w3 >= x1 + w1 >= x3 and y3 + h3 >= y1 + h1 >= y3:
        return True

    if x4 + w4 >= x1 >= x4 and y4 + h4 >= y1 >= y4:
        return True
    elif x4 + w4 >= x1 + w1 >= x4 and y4 + h4 >= y1 >= y4:
        return True
    elif x4 + w4 >= x1 >= x4 and y4 + h4 >= y1 + h1 >= y4:
        return True
    elif x4 + w4 >= x1 + w1 >= x4 and y4 + h4 >= y1 + h1 >= y4:
        return True
    else:
        return False


def down():
    global point, num1, num2, num3
    if sprite2.y == 600:
        sprite2.y, sprite3.y, sprite4.y = 0, 0, 0
        num1 = random.randrange(75, 525, 3)
        num2 = random.randrange(75, 525, 5)
        num3 = random.randrange(75, 525, 7)
        sprite2.x, sprite3.x, sprite4.x = num1, num2, num3
        point += 1



red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


class Sprite:
    def __init__(self, x=270, y=480, height=50, width=50, color=black):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.image = pygame.image.load("sad.png")

    def spec(self):
        gameDisplay.blit(self.image, (self.x, self.y))

    def render(self):
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.height, self.width))


num1 = random.randrange(75, 525, 3)
num2 = random.randrange(75, 525, 5)
num3 = random.randrange(75, 525, 7)

sprite1 = Sprite()
sprite2 = Sprite(num1, 0, 75, 75, red)
sprite3 = Sprite(num2, 0, 75, 75, red)
sprite4 = Sprite(num3, 0, 75, 75, red)

moveX = 0

gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX = -4
            if event.key == pygame.K_RIGHT:
                moveX = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveX = 0
            if event.key == pygame.K_RIGHT:
                moveX = 0

    gameDisplay.fill(white)
    gameDisplay.blit(bg, (0, 0))

    sprite1.x += moveX

    if sprite1.x < 0:
        sprite1.x = 0
    if sprite1.x > 550:
        sprite1.x = 550

    font = pygame.font.SysFont("ComicSansMs", 42)
    text = font.render(str(point), True, (255, 255, 255))

    sprite2.y += 6
    sprite3.y += 6
    sprite4.y += 6

    collisions = detect(sprite1.x, sprite1.y, sprite1.width, sprite1.height,
                        sprite2.x, sprite2.y, sprite2.width, sprite2.height,
                        sprite3.x, sprite3.y, sprite3.width, sprite3.height,
                        sprite4.x, sprite4.y, sprite4.width, sprite4.height)

    if collisions is True:
        gameLoop = False

    sprite1.spec()
    sprite2.render()
    sprite3.render()
    sprite4.render()

    gameDisplay.blit(text, (545 - text.get_width() // 2, 55 - text.get_height() // 2))
    pygame.display.flip()
    down()
    clock.tick(60)
tkinter.messagebox.showinfo("Point", "Your Point : "+str(point))
pygame.quit()