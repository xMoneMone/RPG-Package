import json
import os

save_file = None


def get_save():
    if not os.path.exists('saved_position.json'):
        return dict()
    with open('saved_position.json') as f:
        data = json.load(f)
        return data


to_save = get_save()


def get_save_by_key(search_key):
    data = get_save()
    if search_key and search_key in get_save():
        return data[search_key]
    elif search_key and search_key in to_save:
        return to_save[search_key]


def save_position(room, player):
    saved = dict()
    saved["room"] = room.name
    saved["player"] = [player.rectangle.x, player.rectangle.y, player.direction]
    for asset in room.all_assets:
        if asset:
            saved[asset.id] = [asset.x, asset.y]
    return saved


def add_to_save(new_info: dict, pos=False):
    if pos:
        to_save['position'] = new_info
    else:
        to_save.update(new_info)


def save():
    with open('saved_position.json', 'w') as file:
        json.dump(to_save, file)
