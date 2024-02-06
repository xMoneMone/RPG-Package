import pygame

from center_asset import CenterAsset
from animation import Animation


class AnimatedObject:
    def __init__(self, background: CenterAsset, frames: list, x: int, y: int, game_settings, name: str = "",
                 text: dict = None, door=None):
        self.name = name
        self.text = text
        self._image = None
        self.frames = frames
        for index, frame in enumerate(frames):
            self.frames[index] = pygame.transform.scale_by(frame, game_settings.SCALE)
            self.frames[index].set_colorkey(game_settings.COLOURKEY)
        self.animation = Animation(game_settings.OBJECTS_ANIMATION_SPEED)
        self.rectangle = self.frames[0].get_rect()
        self.og_x = background.x + x * game_settings.SCALE
        self.og_y = background.y + y * game_settings.SCALE
        self.rectangle.x, self.rectangle.y = (self.og_x, self.og_y)
        self.last_frame = self.animation.animate(self.frames)
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

    @property
    def image(self):
        frame = self.animation.animate(self.frames)
        if frame:
            self.last_frame = frame
            return frame
        else:
            return self.last_frame
