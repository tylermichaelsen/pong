import pygame 

class BoxShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.width = width
        self.height = height

    def draw(self, screen):
        pass

    def update(self, dt):
        pass


    #Add collision check 
    def collision_check(self, other):
        selfRight = self.position.x + (self.width / 2)
        selfLeft = self.position.x - (self.width / 2)
        selfTop = self.position.y + (self.height / 2)
        selfBottom = self.position.y - (self.height / 2)

        otherRight = other.position.x + (other.width / 2)
        otherLeft = other.position.x - (other.width / 2)
        otherTop = other.position.y + (other.height / 2)
        otherBottom = other.position.y - (other.height / 2)
        
        return selfLeft >= otherRight and selfRight <= otherLeft and selfBottom >= otherTop and selfTop <= otherBottom 