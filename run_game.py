import pygame
from settings import GameSettings
from interaction import execute_interaction
from draw_room import draw_room
from center_asset import CenterAsset


def run_game(game_settings: GameSettings, rooms: dict, interactions=None, player=None, insert_loop=None,
             insert_outside=None):
    pygame.init()

    game_screen = pygame.display.set_mode((game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
    room = list(rooms.values())[0]
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

    if insert_outside:
        insert_outside()

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
                    interaction = execute_interaction(room, interactions, player)
                    if interaction and interaction[0] == "door":
                        room = rooms[interaction[1].to]
                        if room.background.image.get_height() > game_settings.SCREEN_HEIGHT or \
                                room.background.image.get_width() > game_settings.SCREEN_WIDTH:
                            for asset in room.all_assets:
                                if asset:
                                    player.rectangle.x = game_settings.SCREEN_WIDTH // 2
                                    player.rectangle.y = game_settings.SCREEN_HEIGHT // 2
                                    if type(asset) == CenterAsset:
                                        asset.x += interaction[1].character_x
                                        asset.y += interaction[1].character_y
                                    else:
                                        asset.rectangle.x += interaction[1].character_x
                                        asset.rectangle.y += interaction[1].character_y
                        else:
                            player.rectangle.x = interaction[1].character_x
                            player.rectangle.y = interaction[1].character_y
                    else:
                        interaction_screen = interaction
            if not player and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                interaction_screen = execute_interaction(room, interactions, player)

        if insert_loop:
            insert_loop()

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
