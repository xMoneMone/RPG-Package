from character import Character
from room import Room

interactions = {

}


def interacting_with(player: Character, room: Room):
    collide_direction = None
    if player.direction == player.settings.UP:
        collide_direction = player.rectangle.midtop
    elif player.direction == player.settings.LEFT:
        collide_direction = player.rectangle.midleft
    elif player.direction == player.settings.DOWN:
        collide_direction = player.rectangle.midbottom
    elif player.direction == player.settings.RIGHT:
        collide_direction = player.rectangle.midright

    for asset in room.collidables:
        if asset.rectangle.collidepoint(collide_direction):
            return asset


def execute_interaction(player: Character, room: Room):
    asset = interacting_with(player, room)

    if asset:
        if asset.name in interactions:
            interactions[asset.name]()
        elif asset.text:
            print(asset.text)
