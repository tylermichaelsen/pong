import pygame
from boxshape import BoxShape

class Player(BoxShape):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 10)
        self.x = x
        self.y = y
        self.timer = 0

    def draw(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.x - (10/2), self.y + (10/2), 10, 10))
        

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y = self.y - (25 * dt)
        if keys[pygame.K_s]:
            self.y = self.y + (25 * dt) 

        self.timer -= dt

        