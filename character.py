import pygame
import os
from animation import Animation
from collisions import colliding
from room import Room


class Character:
    def __init__(self, pos_x: int, pos_y: int, screen: pygame.Surface, game_settings, player_settings):
        self.settings = player_settings
        self.game_settings = game_settings
        self.moving_character_frames = {
            "up": [],
            "down": [],
            "left": [],
            "right": [],
            "up-left": [],
            "up-right": []
        }
        self.still_character_frames = {}
        self.load_character_animation()
        self.height = self.still_character_frames["down"].get_height()
        self.width = self.still_character_frames["down"].get_width()
        self.rectangle = pygame.Rect(pos_x, pos_y, self.width, self.height // self.settings.HITBOX_RATIO)
        self.direction = "down"
        self.animation = Animation(self.settings.ANIMATION_SPEED)
        self.screen = screen
        self.image = self.still_character_frames["down"]

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
            self.direction = "up-right"
        elif (pressed[pygame.K_LEFT] and pressed[pygame.K_UP]) or (pressed[pygame.K_a] and pressed[pygame.K_w]):
            self.direction = "up-left"
        elif (pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]) or (pressed[pygame.K_d] and pressed[pygame.K_s]):
            self.direction = "right"
        elif (pressed[pygame.K_LEFT] and pressed[pygame.K_DOWN]) or (pressed[pygame.K_a] and pressed[pygame.K_s]):
            self.direction = "left"
        elif (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and pressed.count(True) == 1:
            self.direction = "down"
        elif (pressed[pygame.K_UP] or pressed[pygame.K_w]) and pressed.count(True) == 1:
            self.direction = "up"
        elif (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and pressed.count(True) == 1:
            self.direction = "left"
        elif (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and pressed.count(True) == 1:
            self.direction = "right"

    def movement(self, room: Room):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT] or pressed[pygame.K_DOWN] or pressed[pygame.K_UP] or \
                pressed[pygame.K_d] or pressed[pygame.K_a] or pressed[pygame.K_s] or pressed[pygame.K_w]:
            new_image = self.animation.animate(self.moving_character_frames[self.direction])
            self.change_direction(pressed)
            if ((pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]) or (
                    pressed[pygame.K_d] and pressed[pygame.K_w])) and not colliding(room, self, "up-right"):
                self.direction = "up-right"
                self.rectangle.x += self.settings.DIAGONAL_SPEED
                self.rectangle.y -= self.settings.DIAGONAL_SPEED
            elif ((pressed[pygame.K_LEFT] and pressed[pygame.K_UP]) or (
                    pressed[pygame.K_a] and pressed[pygame.K_w])) and not colliding(room, self, "up-left"):
                self.direction = "up-left"
                self.rectangle.x -= self.settings.DIAGONAL_SPEED
                self.rectangle.y -= self.settings.DIAGONAL_SPEED
            elif ((pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]) or (
                    pressed[pygame.K_d] and pressed[pygame.K_s])) and not colliding(room, self, "down-right"):
                self.direction = "right"
                self.rectangle.x += self.settings.DIAGONAL_SPEED
                self.rectangle.y += self.settings.DIAGONAL_SPEED
            elif ((pressed[pygame.K_LEFT] and pressed[pygame.K_DOWN]) or (
                    pressed[pygame.K_a] and pressed[pygame.K_s])) and not colliding(room, self, "down-left"):
                self.direction = "left"
                self.rectangle.x -= self.settings.DIAGONAL_SPEED
                self.rectangle.y += self.settings.DIAGONAL_SPEED
            elif (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and pressed.count(True) == 1 and not colliding(
                    room, self, "down"):
                self.direction = "down"
                self.rectangle.y += self.settings.MOVEMENT_SPEED
            elif (pressed[pygame.K_UP] or pressed[pygame.K_w]) and pressed.count(True) == 1 and not colliding(
                    room, self, "up"):
                self.direction = "up"
                self.rectangle.y -= self.settings.MOVEMENT_SPEED
            elif (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and pressed.count(True) == 1 and not colliding(
                    room, self, "left"):
                self.direction = "left"
                self.rectangle.x -= self.settings.MOVEMENT_SPEED
            elif (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and pressed.count(True) == 1 and not colliding(
                    room, self, "right"):
                self.direction = "right"
                self.rectangle.x += self.settings.MOVEMENT_SPEED

            if new_image:
                self.image = new_image
        else:
            self.image = self.still_character_frames[self.direction]

        self.screen.blit(self.image,
                         (self.rectangle.x, self.rectangle.y - ((self.height // self.settings.HITBOX_RATIO) * 2)))
