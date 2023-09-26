import pygame
from constants import SCALE, COLOURKEY


class CollisionAsset:
    def __init__(self, background, image, x, y, name):
        self.name = name
        self.image = image
        self.image = pygame.transform.scale_by(self.image, SCALE)
        self.image.set_colorkey(COLOURKEY)
        self.rectangle = self.image.get_rect()
        self.x = background.x + x * SCALE
        self.y = background.y + y * SCALE
        self.rectangle.x, self.rectangle.y = (self.x, self.y)
