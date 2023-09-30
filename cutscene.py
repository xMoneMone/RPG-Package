import pygame
from interaction import Interaction
from settings import GameSettings
import json


class Cutscene(Interaction):
    def __init__(self, cutscene_json_path: str, dialogue_key: dict, game_settings: GameSettings, image_scale: int = 1,
                 image_margin_bottom=0, cg_dir="", prioroty=1, background_color=None):
        super().__init__(prioroty)
        self.cutscene = json.load(open(cutscene_json_path))['dialogue']
        self.music = json.load(open(cutscene_json_path))['music']
        self.dialogue_key = dialogue_key
        self.settings = game_settings
        self.image_margin_bottom = image_margin_bottom
        self.image_scale = image_scale
        self.current_part_number = 0
        self.cg_dir = cg_dir
        self.background_color = background_color
        if not self.cg_dir:
            self.cg_dir = self.settings.CGS_PATH
        if not self.background_color:
            self.background_color = self.settings.COLOURKEY

    def functionality(self, asset) -> pygame.Surface:
        current_part = self.cutscene[self.current_part_number]

        surface = pygame.Surface((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        surface.fill(self.background_color)

        if not self.open and self.music:
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.music))
        self.open = True

        if "image" in current_part:
            image = pygame.image.load(fr"{self.cg_dir}\{current_part['image']}")
            image = pygame.transform.scale_by(image, self.image_scale)
            image_x = self.settings.SCREEN_WIDTH // 2 - image.get_width() // 2
            image_y = self.settings.SCREEN_HEIGHT // 2 - image.get_height() // 2 + self.image_margin_bottom
            surface.blit(image, (image_x, image_y))

        if "text" in current_part:
            current_dialogue = self.dialogue_key[current_part['speaker']]
            current_dialogue_surface = current_dialogue.functionality(current_part['text'])
            if not current_dialogue_surface:
                self.current_part_number += 1
                if self.current_part_number == len(self.cutscene):
                    self.open = False
                    self.current_part_number = 0
                    pygame.mixer.Channel(1).stop()
                    pygame.mixer.Channel(0).unpause()
                    return
                return self.functionality(asset)
            if current_dialogue_surface:
                surface.blit(current_dialogue_surface, (0, 0))
            if not current_dialogue_surface:
                self.current_part_number += 1
        else:
            self.current_part_number += 1

        if self.current_part_number == len(self.cutscene):
            self.open = False
            self.current_part_number = 0
            pygame.mixer.Channel(1).stop()
            pygame.mixer.Channel(0).unpause()

        surface.set_colorkey(self.settings.COLOURKEY)

        return surface
