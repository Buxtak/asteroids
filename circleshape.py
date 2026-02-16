"""
Code provided by the lesson.
"Throughout this project, we will provide some of the code for you, like the class below.
We want you to focus on OOP concepts not the game physics.
As such, we've pre-written some of the code you'll need, like the CircleShape class below.

"""

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
