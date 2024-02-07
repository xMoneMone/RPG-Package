import pygame
from center_asset import CenterAsset


class StaticObject:
    def __init__(self, background: CenterAsset, image: pygame.Surface, x: int, y: int, game_settings, id,
                 name: str = "", text: dict = None, door=None):
        self.id = id
        self.name = name
        self.text = text
        self.image = image
        self.image = pygame.transform.scale_by(self.image, game_settings.SCALE)
        self.image.set_colorkey(game_settings.COLOURKEY)
        self.rectangle = self.image.get_rect()
        self.og_x = background.x + x * game_settings.SCALE
        self.og_y = background.y + y * game_settings.SCALE
        self.rectangle.x, self.rectangle.y = (self.og_x, self.og_y)
        self.door = door

    @property
    def x(self):
        return self.rectangle.x

    @property
    def y(self):
        return self.rectangle.y

    @x.setter
    def x(self, new_x):
        self.rectangle.x = new_x

    @y.setter
    def y(self, new_y):
        self.rectangle.y = new_y
