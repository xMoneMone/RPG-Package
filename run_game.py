import pygame
from settings import GameSettings
from interaction import execute_interaction
from draw_room import draw_room
from door import check_room_change
from save import save, get_save, save_position, add_to_save
import os
from utility import Fade


def run_game(game_settings: GameSettings, rooms: dict, interactions=None, player=None, insert_loop=None,
             insert_outside=None):
    pygame.init()

    game_screen = pygame.display.set_mode((game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
    room = list(rooms.values())[0]
    interaction = None
    pygame.display.set_caption(game_settings.CAPTION)
    fade = Fade(game_settings)
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

    # load room from save file
    if player.settings.SAVE_POSITION and os.path.exists('saved_position.json'):
        data = get_save()['position']
        room = rooms[data['room']]
        player.rectangle.x, player.rectangle.y, player.direction = data['player']
        for asset in room.all_assets:
            if asset:
                asset.x, asset.y = data[str(asset.id)]

    if insert_outside:
        insert_outside()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if player.settings.SAVE_POSITION:
                    add_to_save(save_position(room=room, player=player), pos=True)
                save()
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if player.settings.SAVE_POSITION:
                        add_to_save(save_position(room=room, player=player), pos=True)
                    save()
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE:
                    interaction = execute_interaction(room, interactions, player)
                    if interaction and interaction[0] != "door":
                        interaction_screen = interaction[1]
            if not player and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                interaction_screen = execute_interaction(room, interactions, player)

        if insert_loop:
            insert_loop()

        new_room = check_room_change(player, room.portals, interaction)
        if new_room:
            fade.fading_out = True
            room = rooms[new_room.to]
            if room.background.image.get_height() > game_settings.SCREEN_HEIGHT or \
                    room.background.image.get_width() > game_settings.SCREEN_WIDTH:
                room.reset_room()
                player.rectangle.x = game_settings.SCREEN_WIDTH // 2
                player.rectangle.y = game_settings.SCREEN_HEIGHT // 2
                for asset in room.all_assets:
                    if asset:
                        asset.x += new_room.character_x
                        asset.y += new_room.character_y
            else:
                player.rectangle.x = new_room.character_x
                player.rectangle.y = new_room.character_y
            interaction = None

        if player:
            player.movement(room)
        draw_room(room, game_screen, player)
        if interaction_screen:
            game_screen.blit(interaction_screen, (0, 0))

        if game_settings.CURSOR_PATH:
            cursor_image_rect.center = pygame.mouse.get_pos()
            game_screen.blit(cursor_image, cursor_image_rect)

        if game_settings.ROOM_FADE:
            game_screen.blit(fade.fade_in(color=game_settings.ROOM_FADE_COLOR, speed=game_settings.ROOM_FADE_SPEED),
                             (0, 0))
            game_screen.blit(fade.fade_out(color=game_settings.ROOM_FADE_COLOR, speed=game_settings.ROOM_FADE_SPEED),
                             (0, 0))

        pygame.display.update()
        clock.tick(game_settings.FPS)
