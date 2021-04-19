import pygame
from random import randint

BLACK = (0,0,0)

class Bubble(pygame.sprite.Sprite):

    def __init__(self,color,radius,center_pos,width,height):

        # Call the parent class (sprite constructor)
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image,color,center_pos,radius)
        self.rect = self.image.get_rect()


    # Every frame the bubble moves randomly
    def update(self):
        self.rect.x += randint(-10,10)
        self.rect.y += randint(-10,10)

        
