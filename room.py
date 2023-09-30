import json
import pygame
import os
from center_asset import CenterAsset
from static_object import StaticObject
from animated_object import AnimatedObject


class Room:
    def __init__(self, name, coordinates_json_path, assets_path, game_settings, interaction_text_json_path="",
                 music_path=""):
        self.name = name
        self.background_color = (255, 255, 255)
        self.background = None
        self.collidables = []
        self.non_collidables = []
        self.light = []
        self.frame = None
        self.coordinates_path = coordinates_json_path
        self.interaction_text_path = interaction_text_json_path
        self.assets_path = assets_path
        self.game_settings = game_settings
        self.music = music_path
        self.load_room()

    def load_room(self):
        with open(self.coordinates_path) as f:
            data = json.load(f)

            with open(self.interaction_text_path) as r_text:
                text = json.load(r_text)

                self.background_color = data["background_color"]

                if "background" in data["center"]:
                    background_image = pygame.image.load(fr"{self.assets_path}\background.png")
                    self.background = CenterAsset(background_image, self.game_settings)

                if "frame" in data["center"]:
                    frame_image = pygame.image.load(fr"{self.assets_path}\frame.png")
                    self.frame = CenterAsset(frame_image, self.game_settings)

                if "light" in data:
                    for asset in data["light"]:
                        light_image = pygame.image.load(fr"{self.assets_path}\{asset}.png")
                        for asset_instance in data["light"][asset]:
                            self.light.append(
                                StaticObject(self.background, light_image, asset_instance[0],
                                             asset_instance[1], self.game_settings))

                for asset in data["no-collision"]:
                    for asset_instance in data["no-collision"][asset]:
                        if os.path.isdir(fr"{self.assets_path}\{asset}"):
                            frames = []
                            for filename in os.listdir(fr"{self.assets_path}\{asset}"):
                                image = pygame.image.load(fr"{self.assets_path}\{asset}\{filename}")
                                frames.append(image)
                            self.non_collidables.append(
                                AnimatedObject(self.background, frames, asset_instance[0],
                                               asset_instance[1], self.game_settings))

                        else:
                            no_col_image = pygame.image.load(fr"{self.assets_path}\{asset}.png")
                            self.non_collidables.append(
                                StaticObject(self.background, no_col_image, asset_instance[0],
                                             asset_instance[1], self.game_settings))

                for asset in data["collision"]:
                    for asset_instance in data["collision"][asset]:
                        if os.path.isdir(fr"{self.assets_path}\{asset}"):
                            frames = []
                            for filename in os.listdir(fr"{self.assets_path}\{asset}"):
                                image = pygame.image.load(fr"{self.assets_path}\{asset}\{filename}")
                                frames.append(image)
                            name = asset
                            if len(asset_instance) == 3:
                                name = asset_instance[2]
                            self.collidables.append(
                                AnimatedObject(self.background, frames, asset_instance[0],
                                               asset_instance[1], self.game_settings, name=name))
                            if asset in text:
                                self.collidables[-1].text = text[name]
                        else:
                            col_image = pygame.image.load(fr"{self.assets_path}\{asset}.png")
                            name = asset
                            if len(asset_instance) == 3:
                                name = asset_instance[2]
                            self.collidables.append(
                                StaticObject(self.background, col_image, asset_instance[0],
                                             asset_instance[1], self.game_settings, name=name))
                            if asset in text:
                                self.collidables[-1].text = text[name]
