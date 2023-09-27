import pygame
import os
from settings import GameSettings
from interaction import Interaction
from static_object import StaticObject


class Dialogue(Interaction):
    def __init__(self, textbox_path: str, game_settings: GameSettings, margin_bottom=0,
                 margin_left=0, margin_right=0, portrait_right=False, portrait_margin_bottom=0,
                 portrait_margin_left=0, portrait_margin_right=0, portraits_path: str = None):
        super().__init__()
        self.settings = game_settings
        self.textbox = pygame.image.load(textbox_path)
        self.textbox = pygame.transform.scale_by(self.textbox, self.settings.SCALE)
        self.textbox.set_colorkey(self.settings.COLOURKEY)
        self.textbox_x = game_settings.SCREEN_WIDTH // 2 - self.textbox.get_width() // 2 - margin_left + margin_right
        self.textbox_y = game_settings.SCREEN_HEIGHT - self.textbox.get_height() - margin_bottom
        self.portraits = {}
        if portraits_path:
            self.load_portrait(portraits_path)
            self.portrait_x = self.textbox_x - self.portraits[
                list(self.portraits.keys())[0]].get_width() // 2 - portrait_margin_left + portrait_margin_right
            if portrait_right:
                self.portrait_x += self.textbox.get_width()
            self.portrait_y = game_settings.SCREEN_HEIGHT - self.portraits[
                list(self.portraits.keys())[0]].get_height() - portrait_margin_bottom

    def load_portrait(self, portraits_path):
        for name in os.listdir(portraits_path):
            file = os.path.join(portraits_path, name)
            if os.path.isfile(file):
                name, *_ = name.split(".")
                image = pygame.image.load(file)
                image = pygame.transform.scale_by(image, self.settings.SCALE)
                image.set_colorkey(self.settings.COLOURKEY)
                self.portraits[name] = image

    def functionality(self, asset: StaticObject):
        asset_dialogue = asset.text

        if not asset_dialogue or self.open:
            return

        self.open = True
        surface = pygame.Surface((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        surface.fill(self.settings.COLOURKEY)
        if self.open:
            surface.blit(self.textbox, (self.textbox_x, self.textbox_y))
            if self.portraits:
                if "emotion" in asset_dialogue:
                    surface.blit(self.portraits[asset_dialogue["emotion"]], (self.portrait_x, self.portrait_y))
                else:
                    surface.blit(self.portraits["default"], (self.portrait_x, self.portrait_y))
        surface.set_colorkey(self.settings.COLOURKEY)
        return surface
