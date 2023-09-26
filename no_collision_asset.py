import pygame
from constants import SCALE, COLOURKEY


class NoCollisionAsset:
    def __init__(self, background, image, x, y):
        self.image = image
        self.image = pygame.transform.scale_by(self.image, SCALE)
        self.image.set_colorkey(COLOURKEY)
        self.x = background.x + x * SCALE
        self.y = background.y + y * SCALE
