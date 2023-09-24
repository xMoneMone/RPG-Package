import json
import pygame
from center_class import Center


class Room:
    def __init__(self, paths, player):
        self.background_color = (255, 255, 255)
        self.background = None
        self.collidables = None
        self.non_collidables = None
        self.light = None
        self.frame = None
        self.load_room(paths, player)

    def draw_room(self, screen, player):
        screen.fill(self.background_color)
        screen.blit(self.background.image, (self.background.x, self.background.y))
        player.movement()
        screen.blit(self.frame.image, (self.frame.x, self.frame.y))

    def load_room(self, paths, player):
        with open(paths['json']) as f:
            data = json.load(f)

            self.background_color = data["background_color"]

            if "background" in data["center"]:
                background_image = pygame.image.load(paths['assets'] + 'background.png')
                self.background = Center(background_image)

            if "frame" in data["center"]:
                frame_image = pygame.image.load(paths['assets'] + 'frame.png')
                self.frame = Center(frame_image)

            player.rectangle.x = self.background.x + data["player_start"][0]
            player.rectangle.y = self.background.y + data["player_start"][1]
