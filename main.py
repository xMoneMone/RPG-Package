import pygame

from character import Character
from constants import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, ROOM_PATHS, CAPTION, ICON, COLOURKEY
from room import Room


def main():
    pygame.init()

    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    icon = pygame.image.load(ICON)
    icon.set_colorkey(COLOURKEY)
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    player = Character(200, 300, game_screen)
    current_room = Room(ROOM_PATHS['house_outside'], player)

    while True:
        for evnt in pygame.event.get():
            if evnt.type == pygame.KEYDOWN:
                if evnt.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        game_screen.fill((0, 0, 0))
        current_room.draw_room(game_screen, player)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
