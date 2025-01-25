import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

player = Player(100, SCREEN_HEIGHT/2)
Player.containers(updatable, drawable)

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
