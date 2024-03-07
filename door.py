class Door:
    def __init__(self, character_pos, room_name):
        self.character_x, self.character_y = character_pos
        self.to = room_name


def check_room_change(player, portals, interaction):
    for portal in portals:
        if player.rectangle.colliderect(portal.rectangle):
            return portal.door
    if interaction and interaction[0] == "door":
        return interaction[-1]
    return None
