import sys
from multiprocessing import Pipe

import pygame

from AsteroidField import *
from asteroids import *
from constants import *
from logger import log_event, log_state
from player import *
from shot import *


def main():
    pygame.init()
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver}")
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}""")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 60
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill("black")
        updatable.update(dt)
        for i in asteroids:
            if i.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for i in drawable:
            i.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
