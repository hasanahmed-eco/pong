import pygame
BLACK = (0,0,0)

# It derives the "sprite" class in Pygame
class Paddle(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle
        pygame.draw.rect(self.image,color,[0,0,width,height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveUp(self,pixels):
        self.rect.y -= pixels
        if self.rect.y<0: self.rect.y=0

    def moveDown(self,pixels):
        self.rect.y += pixels
        if self.rect.y>400: self.rect.y = 400
