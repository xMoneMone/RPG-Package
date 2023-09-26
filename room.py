import json
import pygame
from center_asset import CenterAsset
from no_collision_asset import NoCollisionAsset
from collision_asset import CollisionAsset


class Room:
    def __init__(self, name, coordinates_json_path, interaction_text_json_path, assets_path, player, game_settings):
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
        self.load_room(player)

    def draw_room(self, screen: pygame.Surface, player):
        screen.fill(self.background_color)
        screen.blit(self.background.image, (self.background.x, self.background.y))
        for col in self.collidables:
            screen.blit(col.image, (col.x, col.y))
        for no_col in self.non_collidables:
            screen.blit(no_col.image, (no_col.x, no_col.y))
        player.movement(self)
        for no_col in self.non_collidables:
            if player.rectangle.bottom <= no_col.y + no_col.image.get_height() + player.settings.COLLISION_MARGIN:
                screen.blit(no_col.image, (no_col.x, no_col.y))
        for col in self.collidables:
            if player.rectangle.y <= col.y:
                screen.blit(col.image, (col.x, col.y))
        for light in self.light:
            screen.blit(light.image, (light.x, light.y), special_flags=pygame.BLEND_ADD)
        screen.blit(self.frame.image, (self.frame.x, self.frame.y))

    def load_room(self, player):
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

                for asset in data["light"]:
                    light_image = pygame.image.load(fr"{self.assets_path}\{asset}.png")
                    for asset_instance in data["light"][asset]:
                        self.light.append(
                            NoCollisionAsset(self.background, light_image, asset_instance[0],
                                             asset_instance[1], self.game_settings))

                for asset in data["no-collision"]:
                    no_col_image = pygame.image.load(fr"{self.assets_path}\{asset}.png")
                    for asset_instance in data["no-collision"][asset]:
                        self.non_collidables.append(
                            NoCollisionAsset(self.background, no_col_image, asset_instance[0],
                                             asset_instance[1], self.game_settings))

                for asset in data["collision"]:
                    no_col_image = pygame.image.load(fr"{self.assets_path}\{asset}.png")
                    for asset_instance in data["collision"][asset]:
                        name = asset
                        if len(asset_instance) == 3:
                            name = asset_instance[2]
                        self.collidables.append(
                            CollisionAsset(self.background, no_col_image, asset_instance[0],
                                           asset_instance[1], name, self.game_settings))
                        if asset in text:
                            self.collidables[-1].text = text[asset]

            player.rectangle.x = self.background.x + data["player_start"][0] * self.game_settings.SCALE
            player.rectangle.y = self.background.y + data["player_start"][1] * self.game_settings.SCALE
