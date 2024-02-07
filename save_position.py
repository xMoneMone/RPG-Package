import json


def save_position(room, player):
    saved = dict()
    saved["room"] = room.name
    saved["player"] = [player.rectangle.x, player.rectangle.y, player.direction]
    for asset in room.all_assets:
        if asset:
            saved[asset.id] = [asset.x, asset.y]
    with open('saved_position.json', 'w') as file:
        json.dump(saved, file)
