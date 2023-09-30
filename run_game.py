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
    if game_settings.CURSOR_PATH:
        pygame.mouse.set_visible(False)
        cursor_image = pygame.image.load(game_settings.CURSOR_PATH)
        cursor_image.set_colorkey(game_settings.COLOURKEY)
        cursor_image_rect = cursor_image.get_rect()
    if room.music:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(room.music), -1)
    pygame.mixer.Channel(0).set_volume(game_settings.MUSIC_VOLUME)
    pygame.mixer.Channel(1).set_volume(game_settings.MUSIC_VOLUME)
    pygame.mixer.Channel(2).set_volume(game_settings.INTERACTION_VOLUME)

    interaction_screen = None

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE:
                    interaction_screen = execute_interaction(room, interactions, player)
            if not player and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                interaction_screen = execute_interaction(room, interactions, player)

        if player:
            player.movement(room)
        draw_room(room, game_screen, player)
        if interaction_screen:
            game_screen.blit(interaction_screen, (0, 0))

        if game_settings.CURSOR_PATH:
            cursor_image_rect.center = pygame.mouse.get_pos()
            game_screen.blit(cursor_image, cursor_image_rect)

        pygame.display.update()
        clock.tick(game_settings.FPS)
