import pygame


class CenterAsset:
    def __init__(self, image: pygame.Surface, game_settings):
        self.image = image
        self.image = pygame.transform.scale_by(self.image, game_settings.SCALE)
        self.image.set_colorkey(game_settings.COLOURKEY)
        self.x = game_settings.SCREEN_WIDTH // 2 - self.image.get_width() // 2
        self.y = game_settings.SCREEN_HEIGHT // 2 - self.image.get_height() // 2
        self.og_x = self.x
        self.og_y = self.y
