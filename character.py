import pygame
import os
from animation import Animation
from collisions import colliding
from room import Room


class Character:
    def __init__(self, pos_x: int, pos_y: int, game_settings, player_settings):
        self.settings = player_settings
        self.game_settings = game_settings
        self.moving_character_frames = {
            self.settings.UP: [],
            self.settings.DOWN: [],
            self.settings.LEFT: [],
            self.settings.RIGHT: [],
            self.settings.UP_LEFT: [],
            self.settings.UP_RIGHT: []
        }
        self.still_character_frames = {}
        self.load_character_animation()
        self.height = self.still_character_frames[self.settings.DOWN].get_height()
        self.width = self.still_character_frames[self.settings.DOWN].get_width()
        self.rectangle = pygame.Rect(pos_x, pos_y, self.width, self.height // self.settings.HITBOX_RATIO)
        self.direction = self.settings.DOWN
        self.animation = Animation(self.settings.ANIMATION_SPEED)
        self.image = self.still_character_frames[self.settings.DOWN]

    def load_character_animation(self):
        for name in os.listdir(self.settings.FRAMES_DIR):
            file = os.path.join(self.settings.FRAMES_DIR, name)
            if os.path.isfile(file):
                name, *_ = name.split(".")
                *name, frame_number = name.split("-")
                name = "-".join(name)
                image = pygame.image.load(file)
                image = pygame.transform.scale_by(image, self.game_settings.SCALE)
                image.set_colorkey(self.game_settings.COLOURKEY)
                self.moving_character_frames[name].append(image)
                if frame_number == "1":
                    self.still_character_frames[name] = image

    def change_direction(self, pressed: tuple):
        if (pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]) or (pressed[pygame.K_d] and pressed[pygame.K_w]):
            self.direction = self.settings.UP_RIGHT
        elif (pressed[pygame.K_LEFT] and pressed[pygame.K_UP]) or (pressed[pygame.K_a] and pressed[pygame.K_w]):
            self.direction = self.settings.UP_LEFT
        elif (pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]) or (pressed[pygame.K_d] and pressed[pygame.K_s]):
            self.direction = self.settings.RIGHT
        elif (pressed[pygame.K_LEFT] and pressed[pygame.K_DOWN]) or (pressed[pygame.K_a] and pressed[pygame.K_s]):
            self.direction = self.settings.LEFT
        elif (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and pressed.count(True) == 1:
            self.direction = self.settings.DOWN
        elif (pressed[pygame.K_UP] or pressed[pygame.K_w]) and pressed.count(True) == 1:
            self.direction = self.settings.UP
        elif (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and pressed.count(True) == 1:
            self.direction = self.settings.LEFT
        elif (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and pressed.count(True) == 1:
            self.direction = self.settings.RIGHT

    def movement(self, room: Room):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT] or pressed[pygame.K_DOWN] or pressed[pygame.K_UP] or \
                pressed[pygame.K_d] or pressed[pygame.K_a] or pressed[pygame.K_s] or pressed[pygame.K_w]:
            new_image = self.animation.animate(self.moving_character_frames[self.direction])
            self.change_direction(pressed)
            if ((pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]) or (
                    pressed[pygame.K_d] and pressed[pygame.K_w])) and not colliding(room, self, self.settings.UP_RIGHT):
                self.direction = self.settings.UP_RIGHT
                self.rectangle.x += self.settings.DIAGONAL_SPEED
                self.rectangle.y -= self.settings.DIAGONAL_SPEED
            elif ((pressed[pygame.K_LEFT] and pressed[pygame.K_UP]) or (
                    pressed[pygame.K_a] and pressed[pygame.K_w])) and not colliding(room, self, self.settings.UP_LEFT):
                self.direction = self.settings.UP_LEFT
                self.rectangle.x -= self.settings.DIAGONAL_SPEED
                self.rectangle.y -= self.settings.DIAGONAL_SPEED
            elif ((pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]) or (
                    pressed[pygame.K_d] and pressed[pygame.K_s])) and not colliding(room, self,
                                                                                    self.settings.DOWN_RIGHT):
                self.direction = self.settings.RIGHT
                self.rectangle.x += self.settings.DIAGONAL_SPEED
                self.rectangle.y += self.settings.DIAGONAL_SPEED
            elif ((pressed[pygame.K_LEFT] and pressed[pygame.K_DOWN]) or (
                    pressed[pygame.K_a] and pressed[pygame.K_s])) and not colliding(room, self,
                                                                                    self.settings.DOWN_LEFT):
                self.direction = self.settings.LEFT
                self.rectangle.x -= self.settings.DIAGONAL_SPEED
                self.rectangle.y += self.settings.DIAGONAL_SPEED
            elif (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and pressed.count(True) == 1 and not colliding(
                    room, self, self.settings.DOWN):
                self.direction = self.settings.DOWN
                self.rectangle.y += self.settings.MOVEMENT_SPEED
            elif (pressed[pygame.K_UP] or pressed[pygame.K_w]) and pressed.count(True) == 1 and not colliding(
                    room, self, self.settings.UP):
                self.direction = self.settings.UP
                self.rectangle.y -= self.settings.MOVEMENT_SPEED
            elif (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and pressed.count(True) == 1 and not colliding(
                    room, self, self.settings.LEFT):
                self.direction = self.settings.LEFT
                self.rectangle.x -= self.settings.MOVEMENT_SPEED
            elif (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and pressed.count(True) == 1 and not colliding(
                    room, self, self.settings.RIGHT):
                self.direction = self.settings.RIGHT
                self.rectangle.x += self.settings.MOVEMENT_SPEED

            if new_image:
                self.image = new_image
        else:
            self.image = self.still_character_frames[self.direction]
