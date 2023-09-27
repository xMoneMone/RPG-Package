import pygame

from room import Room
import weakref
from static_object import StaticObject


def interacting_with(room: Room, player=None):
    if player:
        if player.direction in (
                player.settings.UP_LEFT, player.settings.UP_RIGHT, player.settings.DOWN_LEFT, player.settings.DOWN_RIGHT):
            return

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
    else:
        for asset in room.collidables:
            if asset.rectangle.collidepoint(pygame.mouse.get_pos()):
                return asset


def execute_interaction(room: Room, interactions: dict = None, player=None):
    asset = interacting_with(room, player)

    if asset:
        if interactions:
            if asset.name in interactions:
                return interactions[asset.name].functionality(asset)
            elif "default" in interactions:
                return interactions["default"].functionality(asset)
        else:
            if player.dialogue:
                return player.dialogue.functionality(asset)


class Interaction:
    instances = weakref.WeakSet()

    def __init__(self):
        self.__class__.instances.add(self)
        self.open = False
        self.finished = True

    def functionality(self, asset: StaticObject) -> pygame.Surface:
        pass
