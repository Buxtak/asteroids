from multiprocessing import Pipe

import pygame

from constants import *
from logger import log_state
from player import *

# Asteroids project from Boot.dev - Using WSL and ZED


def main():
    pygame.init()
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver}")
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}""")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 60
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
