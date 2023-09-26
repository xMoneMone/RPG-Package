from character import Character
from room import Room

interactions = {

}


def interacting_with(player: Character, room: Room):
    all_colliding = []
    for asset in room.collidables:
        if player.rectangle.colliderect(asset.rectangle):
            all_colliding.append(asset)

    if player.direction == player.settings.UP:
        all_colliding = sorted(all_colliding, key=lambda x: abs(x.rectangle.bottom - player.rectangle.midtop[1]))
    elif player.direction == player.settings.LEFT:
        all_colliding = sorted(all_colliding, key=lambda x: abs(x.rectangle.right - player.rectangle.midtop[0]))
    elif player.direction == player.settings.DOWN:
        all_colliding = sorted(all_colliding, key=lambda x: abs(x.rectangle.top - player.rectangle.midtop[1]))
    elif player.direction == player.settings.RIGHT:
        all_colliding = sorted(all_colliding, key=lambda x: abs(x.rectangle.left - player.rectangle.midtop[0]))

    if all_colliding:
        return all_colliding[0]


def execute_interaction(player: Character, room: Room):
    asset = interacting_with(player, room)

    if asset:
        if asset.name in interactions:
            interactions[asset.name]()
        elif asset.text:
            print(asset.text)
