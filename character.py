import pygame
from load_character_animation import still_character_frames, moving_character_frames
from constants import SPEED, CHARACTER_ANIMATION_SPEED, DIAGONAL_SPEED
from animation import Animation
from collisions import colliding


class Character:
    def __init__(self, pos_x, pos_y, screen: pygame.Surface):
        self.height = still_character_frames["down"].get_height()
        self.width = still_character_frames["down"].get_width()
        self.rectangle = pygame.Rect(pos_x, pos_y, self.width, self.height // 3)
        self.direction = "down"
        self.animation = Animation(CHARACTER_ANIMATION_SPEED)
        self.screen = screen
        self.image = still_character_frames["down"]

    def change_direction(self, pressed):
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

    def movement(self, room):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT] or pressed[pygame.K_DOWN] or pressed[pygame.K_UP] or \
                pressed[pygame.K_d] or pressed[pygame.K_a] or pressed[pygame.K_s] or pressed[pygame.K_w]:
            new_image = self.animation.animate(moving_character_frames[self.direction])
            self.change_direction(pressed)
            if ((pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]) or (
                    pressed[pygame.K_d] and pressed[pygame.K_w])) and not colliding(room, self, "up-right"):
                self.direction = "up-right"
                self.rectangle.x += DIAGONAL_SPEED
                self.rectangle.y -= DIAGONAL_SPEED
            elif ((pressed[pygame.K_LEFT] and pressed[pygame.K_UP]) or (
                    pressed[pygame.K_a] and pressed[pygame.K_w])) and not colliding(room, self, "up-left"):
                self.direction = "up-left"
                self.rectangle.x -= DIAGONAL_SPEED
                self.rectangle.y -= DIAGONAL_SPEED
            elif ((pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]) or (
                    pressed[pygame.K_d] and pressed[pygame.K_s])) and not colliding(room, self, "down-right"):
                self.direction = "right"
                self.rectangle.x += DIAGONAL_SPEED
                self.rectangle.y += DIAGONAL_SPEED
            elif ((pressed[pygame.K_LEFT] and pressed[pygame.K_DOWN]) or (
                    pressed[pygame.K_a] and pressed[pygame.K_s])) and not colliding(room, self, "down-left"):
                self.direction = "left"
                self.rectangle.x -= DIAGONAL_SPEED
                self.rectangle.y += DIAGONAL_SPEED
            elif (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and pressed.count(True) == 1 and not colliding(
                    room, self, "down"):
                self.direction = "down"
                self.rectangle.y += SPEED
            elif (pressed[pygame.K_UP] or pressed[pygame.K_w]) and pressed.count(True) == 1 and not colliding(
                    room, self, "up"):
                self.direction = "up"
                self.rectangle.y -= SPEED
            elif (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and pressed.count(True) == 1 and not colliding(
                    room, self, "left"):
                self.direction = "left"
                self.rectangle.x -= SPEED
            elif (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and pressed.count(True) == 1 and not colliding(
                    room, self, "right"):
                self.direction = "right"
                self.rectangle.x += SPEED

            if new_image:
                self.image = new_image
        else:
            self.image = still_character_frames[self.direction]

        self.screen.blit(self.image, (self.rectangle.x, self.rectangle.y - ((self.height // 3) * 2)))
