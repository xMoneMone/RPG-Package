import pygame
import os
from constants import COLOURKEY, SCALE, CHARACTER_FRAMES_DIR

moving_character_frames = {"up": [],
                           "down": [],
                           "left": [],
                           "right": [],
                           "up-left": [],
                           "up-right": []}

still_character_frames = {}

for name in os.listdir(CHARACTER_FRAMES_DIR):
    file = os.path.join(CHARACTER_FRAMES_DIR, name)
    if os.path.isfile(file):
        name, *_ = name.split(".")
        *name, frame_number = name.split("-")
        name = "-".join(name)
        image = pygame.image.load(file)
        image = pygame.transform.scale(image, (image.get_width() * SCALE, image.get_height() * SCALE))
        image.set_colorkey(COLOURKEY)
        moving_character_frames[name].append(image)
        if frame_number == "1":
            still_character_frames[name] = image
