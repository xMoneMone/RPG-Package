from room import Room


def colliding_with(sprite, player):
    collision = player.rectangle.colliderect(sprite.rectangle)
    if collision:
        if abs(sprite.rectangle.left - player.rectangle.right) <= player.settings.COLLISION_MARGIN and \
                player.direction in (player.settings.RIGHT, player.settings.UP_RIGHT, player.settings.DOWN_RIGHT):
            return True
        elif abs(sprite.rectangle.top - player.rectangle.bottom) <= player.settings.COLLISION_MARGIN and \
                player.direction in (player.settings.DOWN, player.settings.DOWN_LEFT, player.settings.DOWN_RIGHT):
            return True
        elif abs(player.rectangle.left - sprite.rectangle.right) <= player.settings.COLLISION_MARGIN and \
                player.direction in (player.settings.LEFT, player.settings.DOWN_LEFT, player.settings.UP_LEFT):
            return True
        elif abs(player.rectangle.top - sprite.rectangle.bottom) <= player.settings.COLLISION_MARGIN and \
                player.direction in (player.settings.UP, player.settings.UP_LEFT, player.settings.UP_RIGHT):
            return True
    return False


def colliding(room: Room, player):
    # room boundaries
    room_bottom = room.background.y + room.background.image.get_height()
    room_right = room.background.x + room.background.image.get_width()
    if room_right - player.rectangle.right <= player.settings.COLLISION_MARGIN and player.direction in (
            player.settings.RIGHT, player.settings.UP_RIGHT, player.settings.DOWN_RIGHT):
        return True
    elif player.rectangle.left - room.background.x <= player.settings.COLLISION_MARGIN and player.direction in (
            player.settings.LEFT, player.settings.UP_LEFT, player.settings.DOWN_LEFT):
        return True
    elif room_bottom - player.rectangle.bottom <= player.settings.COLLISION_MARGIN and player.direction in (
            player.settings.DOWN, player.settings.DOWN_RIGHT, player.settings.DOWN_LEFT):
        return True
    elif player.rectangle.top - room.background.y <= player.settings.COLLISION_MARGIN and player.direction in (
            player.settings.UP, player.settings.UP_RIGHT, player.settings.UP_LEFT):
        return True

    # sprite collissions
    for sprite in room.collidables:
        result = colliding_with(sprite, player)
        if result:
            return result

    return False
