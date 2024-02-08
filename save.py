import json

save_file = None


def save_position(room, player):
    saved = dict()
    saved["room"] = room.name
    saved["player"] = [player.rectangle.x, player.rectangle.y, player.direction]
    for asset in room.all_assets:
        if asset:
            saved[asset.id] = [asset.x, asset.y]
    return saved


def save(room=None, player=None, to_save: dict = None):
    saved = dict()
    if room and player:
        saved['position'] = save_position(room, player)
    if to_save:
        saved.update(to_save)
    with open('saved_position.json', 'w') as file:
        json.dump(saved, file)


def get_save():
    with open('saved_position.json') as f:
        data = json.load(f)
        return data
