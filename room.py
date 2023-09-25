import json
import pygame
from center_asset import CenterAsset
from no_collision_asset import NoCollisionAsset
from constants import SCALE


class Room:
    def __init__(self, paths, player):
        self.background_color = (255, 255, 255)
        self.background = None
        self.collidables = []
        self.non_collidables = []
        self.light = []
        self.frame = None
        self.load_room(paths, player)

    def draw_room(self, screen, player):
        screen.fill(self.background_color)
        screen.blit(self.background.image, (self.background.x, self.background.y))
        for col in self.collidables:
            screen.blit(col.image, (col.x, col.y))
        player.movement()
        for no_col in self.non_collidables:
            screen.blit(no_col.image, (no_col.x, no_col.y))
        for light in self.light:
            screen.blit(light.image, (light.x, light.y), special_flags=pygame.BLEND_ADD)
        screen.blit(self.frame.image, (self.frame.x, self.frame.y))

    def load_room(self, paths, player):
        with open(paths['json']) as f:
            data = json.load(f)

            self.background_color = data["background_color"]

            if "background" in data["center"]:
                background_image = pygame.image.load(fr"{paths['assets']}\background.png")
                self.background = CenterAsset(background_image)

            if "frame" in data["center"]:
                frame_image = pygame.image.load(fr"{paths['assets']}\frame.png")
                self.frame = CenterAsset(frame_image)

            for asset in data["light"]:
                light_image = pygame.image.load(fr"{paths['assets']}\{asset}.png")
                self.light.append(
                    NoCollisionAsset(self.background, light_image, data["light"][asset][0][0], data["light"][asset][0][1]))

            for asset in data["no-collision"]:
                no_col_image = pygame.image.load(fr"{paths['assets']}\{asset}.png")
                self.non_collidables.append(
                    NoCollisionAsset(self.background, no_col_image, data["no-collision"][asset][0][0],
                                     data["no-collision"][asset][0][1]))

            for asset in data["collision"]:
                no_col_image = pygame.image.load(fr"{paths['assets']}\{asset}.png")
                self.collidables.append(
                    NoCollisionAsset(self.background, no_col_image, data["collision"][asset][0][0],
                                     data["collision"][asset][0][1]))

            player.rectangle.x = self.background.x + data["player_start"][0] * SCALE
            player.rectangle.y = self.background.y + data["player_start"][1] * SCALE
