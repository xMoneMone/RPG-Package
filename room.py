import json
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from background_class import Background


class Room:
    def __init__(self, paths):
        self.background_color = (255, 255, 255)
        self.background = None
        self.collidables = None
        self.non_collidables = None
        self.light = None
        self.frame = None
        self.load_room(paths)

    def draw_room(self, screen, player):
        screen.fill(self.background_color)
        screen.blit(self.background.image, (self.background.x, self.background.y))
        player.movement()

    def load_room(self, paths):
        with open(paths['json']) as f:
            data = json.load(f)
            self.background_color = data["background_color"]
            background_image = pygame.image.load(paths['assets'] + 'background.png')
            background_image_w = background_image.get_width()
            background_image_h = background_image.get_height()
            self.background = Background(background_image,
                                         SCREEN_WIDTH // 2 - background_image_w // 2,
                                         SCREEN_HEIGHT // 2 - background_image_h // 2)
