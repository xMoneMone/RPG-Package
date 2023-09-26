from collections import namedtuple

import pygame

pygame.init()

# general
FPS = 60
SCALE = 2
COLOURKEY = (255, 75, 248)
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
ICON = r"graphics\character_frames\down-1.png"
CAPTION = "Game"

# player
clock = pygame.time.Clock()
dt = clock.tick(FPS)
SPEED = 600 * (dt / 1000)
DIAGONAL_SPEED = SPEED / (2 ** 0.5)
CHARACTER_ANIMATION_SPEED = 50
CHARACTER_FRAMES_DIR = r"graphics\character_frames"
COLLISION_MARGIN = 10

# rooms
Room = namedtuple('Room', ['json', 'assets'])
ROOM_PATHS = {
    'house_outside': Room(json=r"json_files\house_outside\coordinates.json",
                          assets=r"graphics\room_assets\house_outside")
}
