import pygame
pygame.init()

# general
FPS = 60
SCALE = 2
COLOURKEY = (255, 75, 248)
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h

# character animation
SPEED = 5
DIAGONAL_SPEED = 3
CHARACTER_ANIMATION_SPEED = 50
CHARACTER_FRAMES_DIR = r"graphics\character_frames"

# rooms
ROOM_PATHS = {
    "house_outside": {
        "json": r"json_files\house_outside\coordinates.json",
        "assets": r"graphics\room_assets\house_outside\\"
    }
}
