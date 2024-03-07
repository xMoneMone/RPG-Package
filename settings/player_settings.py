import pygame


class PlayerSettings:
    def __init__(self, animation_frames_path, fps=60, movement_speed=600, animation_speed=50, collision_margin=10,
                 hitbox_ratio=3, up="up", down="down", left="left", right="right", upleft="up-left", upright="up-right",
                 downleft="down-left", downright="down-right", save_position=False):
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(fps)
        self.MOVEMENT_SPEED = movement_speed * (self.dt / 1000)
        self.DIAGONAL_SPEED = self.MOVEMENT_SPEED / (2 ** 0.5)
        self.ANIMATION_SPEED = animation_speed
        self.FRAMES_DIR = animation_frames_path
        self.COLLISION_MARGIN = collision_margin
        self.HITBOX_RATIO = hitbox_ratio
        self.UP = up
        self.DOWN = down
        self.LEFT = left
        self.RIGHT = right
        self.DOWN_LEFT = downleft
        self.UP_LEFT = upleft
        self.DOWN_RIGHT = downright
        self.UP_RIGHT = upright
        self.SAVE_POSITION = save_position
