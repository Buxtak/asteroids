import pygame

from constants import *
from logger import log_state

# Asteroids project from Boot.dev - Using WSL and ZED


def main():
    pygame.init()
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver}")
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}""")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 60

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            clock.tick(60)
            dt = clock.tick(60) / 1000

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
