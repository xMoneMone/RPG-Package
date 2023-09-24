import pygame
from load_character_animation import still_character_frames, moving_character_frames
from constants import SPEED, CHARACTER_ANIMATION_SPEED, DIAGONAL_SPEED
from animation import Animation


class Character:
    def __init__(self, pos_x, pos_y, screen: pygame.Surface):
        self.height = still_character_frames["down"].get_height()
        self.width = still_character_frames["down"].get_width()
        self.rectangle = pygame.Rect(pos_x, pos_y, self.width, self.height // 3)
        self.direction = "down"
        self.animation = Animation(CHARACTER_ANIMATION_SPEED)
        self.screen = screen
        self.image = still_character_frames["down"]

    def movement(self):
        pressed = pygame.key.get_pressed()

        if any(pressed):
            new_image = self.animation.animate(moving_character_frames[self.direction])
            if pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]:
                self.direction = "up-right"
                self.rectangle.x += DIAGONAL_SPEED
                self.rectangle.y -= DIAGONAL_SPEED
            elif pressed[pygame.K_LEFT] and pressed[pygame.K_UP]:
                self.direction = "up-left"
                self.rectangle.x -= DIAGONAL_SPEED
                self.rectangle.y -= DIAGONAL_SPEED
            elif pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]:
                self.direction = "right"
                self.rectangle.x += DIAGONAL_SPEED
                self.rectangle.y += DIAGONAL_SPEED
            elif pressed[pygame.K_LEFT] and pressed[pygame.K_DOWN]:
                self.direction = "left"
                self.rectangle.x -= DIAGONAL_SPEED
                self.rectangle.y += DIAGONAL_SPEED
            elif pressed[pygame.K_DOWN] and pressed.count(True) == 1:
                self.direction = "down"
                self.rectangle.y += SPEED
            elif pressed[pygame.K_UP] and pressed.count(True) == 1:
                self.direction = "up"
                self.rectangle.y -= SPEED
            elif pressed[pygame.K_LEFT] and pressed.count(True) == 1:
                self.direction = "left"
                self.rectangle.x -= SPEED
            elif pressed[pygame.K_RIGHT] and pressed.count(True) == 1:
                self.direction = "right"
                self.rectangle.x += SPEED

            if new_image:
                self.image = new_image
        else:
            self.image = still_character_frames[self.direction]

        self.screen.blit(self.image, (self.rectangle.x, self.rectangle.y))
