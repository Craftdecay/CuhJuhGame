import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640,640))

guy_png = pygame.image.load('guy.png').convert()
guy_png = pygame.transform.scale(guy_png,
                                (guy_png.get_width() * 2, 
                                 guy_png.get_height() * 2))

running = True
x = 0
clock = pygame.time.Clock()
delta_time = 0.1
y = 30
font = pygame.font.Font(None, size=30)
right = False
left = False
up = False
down = False
while running:
    screen.fill((0, 0, 0))

    screen.blit(guy_png, (x, y))

    hitbox = pygame.Rect(x, y, guy_png.get_width(), guy_png.get_height())

    target = pygame.Rect(300, 0, 160, 280)
    collision = hitbox.colliderect(target)
    pygame.draw.rect(screen, (255 * collision, 255, 0), target)
    if right:
        x += 50 * delta_time
    if left:
        x -= 50 * delta_time
    if down:
        y += 50 * delta_time
    if up:
        y -= 50 * delta_time
    
    text = font.render('Goofy Game', True, (255, 255, 255))
    screen.blit(text, (300, 100))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                right = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                down = False
    
    pygame.display.flip()

    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()