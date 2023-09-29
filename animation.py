import pygame


class Animation:
    def __init__(self, waiting_time: int):
        self.waiting_time = waiting_time
        self.last_update = pygame.time.get_ticks()
        self.frame = -1

    def animate(self, frames_list):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.waiting_time:
            if self.frame >= len(frames_list)-1:
                self.frame = -1
            self.frame += 1
            self.last_update = current_time
            if frames_list:
                return frames_list[self.frame]
