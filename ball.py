import pygame
from boxshape import BoxShape
from constants import BALL_SPEED, BALL_HEIGHT, BALL_WIDTH

class Ball(BoxShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_WIDTH, BALL_HEIGHT)
        self.position = pygame.Vector2(x,y)

    def draw(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.position.x - (BALL_WIDTH/2), self.position.y + (BALL_HEIGHT/2), BALL_WIDTH, BALL_HEIGHT))

    def update(self, dt):
        self.position += (self.velocity * dt)