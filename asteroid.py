from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, ASTEROID_MAX_RADIUS)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), 2)

    