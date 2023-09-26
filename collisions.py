from room import Room


def colliding(room: Room, player, player_direction: str):
    # room boundaries
    room_bottom = room.background.y + room.background.image.get_height()
    room_right = room.background.x + room.background.image.get_width()
    if room_right - player.rectangle.right <= player.settings.COLLISION_MARGIN and player_direction in (
            "right", "up-right", "down-right"):
        return True
    elif player.rectangle.left - room.background.x <= player.settings.COLLISION_MARGIN and player_direction in (
            "left", "up-left", "down-left"):
        return True
    elif room_bottom - player.rectangle.bottom <= player.settings.COLLISION_MARGIN and player_direction in (
            "down", "down-right", "down-left"):
        return True
    elif player.rectangle.top - room.background.y <= player.settings.COLLISION_MARGIN and player_direction in (
            "up", "up-right", "up-left"):
        return True

    # sprite collissions
    for sprite in room.collidables:
        collision = player.rectangle.colliderect(sprite.rectangle)
        if collision:
            if abs(sprite.rectangle.left - player.rectangle.right) <= player.settings.COLLISION_MARGIN and \
                    player_direction in ("right", "up-right", "down-right"):
                return True
            elif abs(sprite.rectangle.top - player.rectangle.bottom) <= player.settings.COLLISION_MARGIN and \
                    player_direction in ("down", "down-left", "down-right"):
                return True
            elif abs(player.rectangle.left - sprite.rectangle.right) <= player.settings.COLLISION_MARGIN and \
                    player_direction in ("left", "down-left", "up-left"):
                return True
            elif abs(player.rectangle.top - sprite.rectangle.bottom) <= player.settings.COLLISION_MARGIN and \
                    player_direction in ("up", "up-left", "up-right"):
                return True

    return False
