import pygame
from center_asset import CenterAsset


class NoCollisionAsset:
    def __init__(self, background: CenterAsset, image: pygame.Surface, x: int, y: int, game_settings):
        self.image = image
        self.image = pygame.transform.scale_by(self.image, game_settings.SCALE)
        self.image.set_colorkey(game_settings.COLOURKEY)
        self.x = background.x + x * game_settings.SCALE
        self.y = background.y + y * game_settings.SCALE
