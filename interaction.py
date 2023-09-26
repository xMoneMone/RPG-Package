from character import Character
from room import Room


def interacting_with(player: Character, room: Room):
    all_colliding = []
    collide_direction = None

    for asset in room.collidables:
        if player.rectangle.colliderect(asset.rectangle):
            all_colliding.append(asset)

    if player.direction == player.settings.UP:
        collide_direction = player.rectangle.midtop
        all_colliding = sorted(all_colliding, key=lambda x: abs(x.rectangle.bottom - player.rectangle.midtop[1]))
    elif player.direction == player.settings.LEFT:
        collide_direction = player.rectangle.midleft
        all_colliding = sorted(all_colliding, key=lambda x: abs(x.rectangle.right - player.rectangle.midtop[0]))
    elif player.direction == player.settings.DOWN:
        collide_direction = player.rectangle.midbottom
        all_colliding = sorted(all_colliding, key=lambda x: abs(x.rectangle.top - player.rectangle.midtop[1]))
    elif player.direction == player.settings.RIGHT:
        collide_direction = player.rectangle.midright
        all_colliding = sorted(all_colliding, key=lambda x: abs(x.rectangle.left - player.rectangle.midtop[0]))

    for asset in room.collidables:
        if asset.rectangle.collidepoint(collide_direction):
            return asset
    if all_colliding:
        return all_colliding[0]


def execute_interaction(player: Character, room: Room, interactions: dict = None):
    asset = interacting_with(player, room)

    if asset:
        if interactions:
            if asset.name in interactions:
                interactions[asset.name]()
        elif asset.text:
            print(asset.text)
