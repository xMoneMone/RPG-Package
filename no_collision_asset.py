import pygame
from constants import SCALE, COLOURKEY
from center_asset import CenterAsset


class NoCollisionAsset:
    def __init__(self, background: CenterAsset, image: pygame.Surface, x: int, y: int):
        self.image = image
        self.image = pygame.transform.scale_by(self.image, SCALE)
        self.image.set_colorkey(COLOURKEY)
        self.x = background.x + x * SCALE
        self.y = background.y + y * SCALE
