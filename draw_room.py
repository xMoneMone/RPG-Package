import pygame


def draw_room(room, screen: pygame.Surface, player):
    screen.fill(room.background_color)
    screen.blit(room.background.image, (room.background.x, room.background.y))
    for col in room.collidables:
        screen.blit(col.image, (col.x, col.y))
    for no_col in room.non_collidables:
        screen.blit(no_col.image, (no_col.x, no_col.y))
    player.movement(room)
    for no_col in room.non_collidables:
        if player.rectangle.bottom <= no_col.y + no_col.image.get_height() + player.settings.COLLISION_MARGIN:
            screen.blit(no_col.image, (no_col.x, no_col.y))
    for col in room.collidables:
        if player.rectangle.y <= col.y:
            screen.blit(col.image, (col.x, col.y))
    for light in room.light:
        screen.blit(light.image, (light.x, light.y), special_flags=pygame.BLEND_ADD)
    screen.blit(room.frame.image, (room.frame.x, room.frame.y))
