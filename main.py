import pygame
from constants import FPS
from character import Character


def main():
    pygame.init()

    monitor = pygame.display.Info()
    width = monitor.current_w
    height = monitor.current_h

    game_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Void Game")

    clock = pygame.time.Clock()

    player = Character(200, 300, game_screen)

    while True:
        for evnt in pygame.event.get():
            if evnt.type == pygame.KEYDOWN:
                if evnt.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        game_screen.fill((0, 0, 0))

        player.movement()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
