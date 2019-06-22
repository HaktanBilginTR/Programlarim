
import pygame

pygame.init()

win = pygame.display.set_mode((0,0),pygame.RESIZABLE)

pygame.display.set_caption("Oyun")
clock = pygame.time.Clock()

class sprite():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = global_color
        self.circle = (x, y)

    def blit(self):
        pygame.draw.circle(win, self.color, self.circle, 15)

global_color = (255,0,0)
game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                global_color = (255,0,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                global_color = (0,255,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                global_color = (0,0,255)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                win.fill((0,0,0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                global_color = (0, 0, 0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                global_color = (255, 255, 255)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                win.fill((255,255,255))



    x = pygame.mouse.get_pressed()
    if x[0] == 1:
        pos = pygame.mouse.get_pos()

        s = sprite(pos[0], pos[1])

        s.blit()

    pygame.display.flip()

    clock.tick(360)







