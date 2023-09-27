import pygame
from center_asset import CenterAsset


class StaticObject:
    def __init__(self, background: CenterAsset, image: pygame.Surface, x: int, y: int, game_settings, name: str = "",
                 text: dict = None):
        self.name = name
        self.text = text
        self.image = image
        self.image = pygame.transform.scale_by(self.image, game_settings.SCALE)
        self.image.set_colorkey(game_settings.COLOURKEY)
        self.rectangle = self.image.get_rect()
        self.x = background.x + x * game_settings.SCALE
        self.y = background.y + y * game_settings.SCALE
        self.rectangle.x, self.rectangle.y = (self.x, self.y)
