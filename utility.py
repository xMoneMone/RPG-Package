import pygame


def fade_in_out(settings, surface, color, fade_in=True, fade_out=True):
    surface.fill((0, 0, 0))
    if fade_in:
        for number in range(0, 300):
            surface.set_alpha(number)
            surface.fill(color)
            pygame.display.update()
            pygame.time.delay(3)
    if fade_out:
        for number in range(300, 0, -1):
            pass

