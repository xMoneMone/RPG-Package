import pygame
from settings import GameSettings
from room import Room
from interaction import execute_interaction
from draw_room import draw_room


def run_game(game_settings: GameSettings, room: Room, interactions=None, player=None):
    pygame.init()

    game_screen = pygame.display.set_mode((game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
    pygame.display.set_caption(game_settings.CAPTION)
    icon = pygame.image.load(game_settings.ICON)
    icon.set_colorkey(game_settings.COLOURKEY)
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    while True:
        for evnt in pygame.event.get():
            if evnt.type == pygame.KEYDOWN:
                if evnt.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if evnt.key == pygame.K_SPACE:
                    if player:
                        if not execute_interaction(player, room, interactions):
                            if player.dialogue:
                                if player.dialogue.open:
                                    player.dialogue.open = False

        if player:
            player.movement(room)
        draw_room(room, game_screen, player)

        pygame.display.update()
        clock.tick(game_settings.FPS)
