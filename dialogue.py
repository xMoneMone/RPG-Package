import pygame
import os
from settings import GameSettings
from interaction import Interaction
from static_object import StaticObject


class Dialogue(Interaction):
    def __init__(self, textbox_path: str, game_settings: GameSettings, margin_bottom=0,
                 margin_left=0, margin_right=0, portrait_right=False, portrait_margin_bottom=0,
                 portrait_margin_left=0, portrait_margin_right=0, portraits_path: str = None,
                 font: str = 'freesansbold.ttf', font_size: int = 32, antialiasing: bool = False,
                 font_color: tuple = (0, 0, 0), font_padding_horizontal: int = 30, font_padding_vertical: int = 30,
                 line_spacing=None):
        super().__init__()
        self.settings = game_settings
        self.textbox = pygame.image.load(textbox_path)
        self.textbox = pygame.transform.scale_by(self.textbox, self.settings.TEXTBOX_SCALE)
        self.textbox.set_colorkey(self.settings.COLOURKEY)
        self.textbox_x = game_settings.SCREEN_WIDTH // 2 - self.textbox.get_width() // 2 - margin_left + margin_right
        self.textbox_y = game_settings.SCREEN_HEIGHT - self.textbox.get_height() - margin_bottom
        self.portraits = {}
        self.font = pygame.font.Font(font, font_size)
        self.font_size = font_size
        self.antialiasing = antialiasing
        self.font_color = font_color
        self.font_x = self.textbox_x + font_padding_horizontal
        self.font_y = self.textbox_y + font_padding_vertical
        self.allowed_text_width = self.textbox.get_width() - font_padding_horizontal
        self.line_spacing = self.font.size("Tg")[1]
        if line_spacing:
            self.line_spacing = line_spacing
        if portraits_path:
            self.load_portrait(portraits_path)
            self.portrait_x = self.textbox_x - self.portraits[
                list(self.portraits.keys())[0]].get_width() // 2 - portrait_margin_left + portrait_margin_right
            if portrait_right:
                self.portrait_x += self.textbox.get_width()
            self.portrait_y = game_settings.SCREEN_HEIGHT - self.portraits[
                list(self.portraits.keys())[0]].get_height() - portrait_margin_bottom
            self.allowed_text_width -= self.portraits[list(self.portraits.keys())[0]].get_width() // 2

    def load_portrait(self, portraits_path):
        for name in os.listdir(portraits_path):
            file = os.path.join(portraits_path, name)
            if os.path.isfile(file):
                name, *_ = name.split(".")
                image = pygame.image.load(file)
                image = pygame.transform.scale_by(image, self.settings.PORTRAIT_SCALE)
                image.set_colorkey(self.settings.COLOURKEY)
                self.portraits[name] = image

    def text_split(self, text):
        text_list = text.split(" ")
        split_lines = []
        space_width = self.font.size(" ")[1]
        current_line = ""

        for index, word in enumerate(text_list):
            word_width = self.font.size(word)[0]
            current_line_width = self.font.size(current_line)[0]
            if current_line_width + space_width + word_width >= self.allowed_text_width or word == "\n":
                split_lines.append(current_line.strip())
                current_line = word
                if index + 1 == len(text_list):
                    split_lines.append(current_line.strip())
                    break
            elif index + 1 == len(text_list):
                current_line += " " + word
                split_lines.append(current_line.strip())
            else:
                current_line += " " + word

        return split_lines

    def functionality(self, asset: StaticObject):
        asset_dialogue = asset.text
        text_y = self.font_y

        if not asset_dialogue or self.open:
            return

        split_text = self.text_split(asset_dialogue['text'])

        text_surface = self.font.render(asset_dialogue['text'], self.antialiasing, self.font_color,
                                        self.settings.COLOURKEY)
        text_surface.set_colorkey(self.settings.COLOURKEY)
        text_rectangle = text_surface.get_rect()
        text_rectangle.topleft = (self.font_x, self.font_y)

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

            for line in split_text:
                text_surface = self.font.render(line, self.antialiasing, self.font_color, self.settings.COLOURKEY)
                text_surface.set_colorkey(self.settings.COLOURKEY)
                text_rectangle = text_surface.get_rect()
                text_rectangle.topleft = (self.font_x, text_y)
                text_y += self.line_spacing
                surface.blit(text_surface, text_rectangle)

        surface.set_colorkey(self.settings.COLOURKEY)
        return surface
