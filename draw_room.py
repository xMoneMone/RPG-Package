import pygame


def check_height(x, player=None):
    if player:
        if x == player:
            return x.rectangle.bottom
        else:
            return x.rectangle.bottom + player.settings.COLLISION_MARGIN

    return x.rectangle.bottom


def draw_room(room, screen: pygame.Surface, player=None):
    all_objects = room.collidables + room.non_collidables
    if player:
        all_objects += [player]
        all_objects = sorted(all_objects, key=lambda x: check_height(x, player))
    else:
        all_objects = sorted(all_objects, key=lambda x: check_height(x))

    screen.fill(room.background_color)
    screen.blit(room.background.image, (room.background.x, room.background.y))

    for obj in all_objects:
        if obj == player:
            screen.blit(obj.image,
                        (obj.rectangle.x, obj.rectangle.y - ((player.height // player.settings.HITBOX_RATIO) * 2)))
        else:
            screen.blit(obj.image, (obj.rectangle.x, obj.rectangle.y))

    for light in room.light:
        screen.blit(light.image, (light.x, light.y), special_flags=pygame.BLEND_ADD)
    if room.frame:
        screen.blit(room.frame.image, (room.frame.x, room.frame.y))
