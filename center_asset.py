import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCALE, COLOURKEY


class CenterAsset(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image = pygame.transform.scale_by(self.image, SCALE)
        self.image.set_colorkey(COLOURKEY)
        self.x = SCREEN_WIDTH // 2 - self.image.get_width() // 2
        self.y = SCREEN_HEIGHT // 2 - self.image.get_height() // 2
