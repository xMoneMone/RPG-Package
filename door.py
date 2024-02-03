class Door:
    def __init__(self, character_pos, room_name):
        self.charcter_x, self.character_y = character_pos
        self.to = room_name
