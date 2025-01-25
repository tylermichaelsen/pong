import pygame
from player import Player
from ball import Ball
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)
player = Player(100, SCREEN_HEIGHT/2)

Ball.containers = (updatable, drawable)
ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for obj in updatable:
        obj.update(dt)

    screen.fill("black")

    for obj in drawable:
        obj.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
