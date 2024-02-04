import json
import pygame
import os
from center_asset import CenterAsset
from static_object import StaticObject
from animated_object import AnimatedObject
from door import Door


class Room:
    def __init__(self, name, coordinates_json_path, assets_path, game_settings, interaction_text_json_path="",
                 music_path=""):
        self.name = name
        self.background_color = (255, 255, 255)
        self.background = None
        self.collidables = []
        self.non_collidables = []
        self.doors = []
        self.light = []
        self.frame = None
        self.coordinates_path = coordinates_json_path
        self.interaction_text_path = interaction_text_json_path
        self.assets_path = assets_path
        self.game_settings = game_settings
        self.music = music_path
        self._all_objects = None
        self._all_assets = None
        self.load_room()
        self.scroll = False

    @property
    def all_objects(self):
        return self.collidables + self.non_collidables

    @property
    def all_assets(self):
        return self.all_objects + self.light + [self.background] + [self.frame]

    def reset_room(self):
        for asset in self.all_assets:
            if asset:
                if type(asset) == CenterAsset:
                    asset.x = asset.og_x
                    asset.y = asset.og_y
                else:
                    asset.rectangle.x = asset.x
                    asset.rectangle.y = asset.y

    def load_room(self):
        with open(self.coordinates_path) as f:
            data = json.load(f)

            with open(self.interaction_text_path) as r_text:
                text = json.load(r_text)

                self.background_color = data["background_color"]

                if "background" in data["center"]:
                    background_image = pygame.image.load(fr"{self.assets_path}\background.png")
                    self.background = CenterAsset(background_image, self.game_settings)
                    if self.background.image.get_height() > self.game_settings.SCREEN_HEIGHT or \
                            self.background.image.get_width() > self.game_settings.SCREEN_WIDTH:
                        self.scroll = True
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

                if "no-collision" in data:
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

                if "collision" in data:
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

                if "door" in data:
                    for asset in data["door"]:
                        pos, character_pos, to_room = data["door"][asset]
                        door = Door(character_pos, to_room)
                        if os.path.isdir(fr"{self.assets_path}\{asset}"):
                            frames = []
                            for filename in os.listdir(fr"{self.assets_path}\{asset}"):
                                image = pygame.image.load(fr"{self.assets_path}\{asset}\{filename}")
                                frames.append(image)
                            name = asset
                            self.collidables.append(
                                AnimatedObject(self.background, frames, pos[0],
                                               pos[1], self.game_settings, name=name, door=door))
                            if asset in text:
                                self.collidables[-1].text = text[name]
                        else:
                            col_image = pygame.image.load(fr"{self.assets_path}\{asset}.png")
                            name = asset
                            self.collidables.append(
                                StaticObject(self.background, col_image, pos[0],
                                             pos[1], self.game_settings, name=name, door=door))
                            if asset in text:
                                self.collidables[-1].text = text[name]
