import pygame

from character import Character
from settings import GameSettings, PlayerSettings
from room import Room
from interaction import execute_interaction


def main():
    pygame.init()

    game_settings = GameSettings(r"graphics\character_frames\down-1.png", scale=2, colourkey=(255, 75, 248),
                                 width=pygame.display.Info().current_w, height=pygame.display.Info().current_h)
    player_settings = PlayerSettings(r"graphics\character_frames")

    game_screen = pygame.display.set_mode((game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
    pygame.display.set_caption(game_settings.CAPTION)
    icon = pygame.image.load(game_settings.ICON)
    icon.set_colorkey(game_settings.COLOURKEY)
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    player = Character(480, 540, game_screen, game_settings, player_settings)
    current_room = Room("house_outside", r"json_files\house_outside\coordinates.json",
                        r"json_files\house_outside\interaction_text.json",
                        r"graphics\room_assets\house_outside",
                        player, game_settings)

    while True:
        for evnt in pygame.event.get():
            if evnt.type == pygame.KEYDOWN:
                if evnt.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if evnt.key == pygame.K_SPACE:
                    execute_interaction(player, current_room)

        game_screen.fill((0, 0, 0))
        current_room.draw_room(game_screen, player)

        pygame.display.update()
        clock.tick(game_settings.FPS)


if __name__ == "__main__":
    main()
