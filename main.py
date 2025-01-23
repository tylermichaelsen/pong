import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
player = Player(1280/2, 720/2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update(dt)

    screen.fill("black")

    player.draw(screen)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
