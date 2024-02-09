import pygame


class Fade:
    def __init__(self, settings):
        self.width = settings.SCREEN_WIDTH
        self.height = settings.SCREEN_HEIGHT
        self.fade_in_intensity = 0
        self.fade_out_intensity = 300
        self.fading_in = False
        self.fading_out = False

    def fade_in(self, color=(0, 0, 0), speed: int = 15):
        surface = pygame.Surface((self.width, self.height))
        surface.set_alpha(self.fade_in_intensity)
        if self.fading_in:
            surface.fill(color)
            self.fade_in_intensity += speed
            if self.fade_in_intensity >= 300:
                self.fade_in_intensity = 0
                self.fading_in = False
        return surface

    def fade_out(self, color=(0, 0, 0), speed: int = 15):
        surface = pygame.Surface((self.width, self.height))
        surface.set_alpha(0)
        if self.fading_out:
            surface.set_alpha(self.fade_out_intensity)
            surface.fill(color)
            self.fade_out_intensity -= speed
            if self.fade_out_intensity <= 0:
                self.fade_out_intensity = 300
                self.fading_out = False
        return surface
