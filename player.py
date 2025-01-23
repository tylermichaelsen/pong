import pygame
from boxshape import BoxShape
from constants import PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_WIDTH

class Player(BoxShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.x = x
        self.y = y
        self.timer = 0

    def draw(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.x - (PLAYER_WIDTH/2), self.y + (PLAYER_HEIGHT/2), PLAYER_WIDTH, PLAYER_HEIGHT))
        

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y = self.y - (PLAYER_SPEED * dt)
        if keys[pygame.K_s]:
            self.y = self.y + (PLAYER_SPEED * dt) 

        self.timer -= dt

        