import pygame


class GameSettings:
    def __init__(self, icon_path, fps=60, scale=1, colourkey=(255, 255, 255),
                 width=220, height=220, caption="Game"):
        self.FPS = fps
        self.SCALE = scale
        self.COLOURKEY = colourkey
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.ICON = icon_path
        self.CAPTION = caption
