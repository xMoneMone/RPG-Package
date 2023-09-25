from constants import COLLISION_MARGIN


def colliding(room, player, player_direction):
    # room boundaries
    room_bottom = room.background.y + room.background.image.get_height()
    room_right = room.background.x + room.background.image.get_width()
    print(room_bottom - player.rectangle.bottom)
    if room_right - player.rectangle.right <= COLLISION_MARGIN and player_direction in (
            "right", "up-right", "down-right"):
        return True
    elif player.rectangle.left - room.background.x <= COLLISION_MARGIN and player_direction in (
            "left", "up-left", "down-left"):
        return True
    elif room_bottom - player.rectangle.bottom <= COLLISION_MARGIN and player_direction in (
            "down", "down-right", "down-left"):
        return True
    elif player.rectangle.top - room.background.y <= COLLISION_MARGIN and player_direction in (
            "up", "up-right", "up-left"):
        return True

    return False
