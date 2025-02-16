import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        # Automatically add the instance to groups in the 'containers' variable
        if hasattr(self.__class__, 'containers'):  # Check if 'containers' is defined
            for group in self.__class__.containers:  # Loop over the groups
                group.add(self)  # Add 'self' to each group

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        vectors = (self.velocity.rotate(random_angle), self.velocity.rotate(-random_angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        for vector in vectors:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = vector * 1.2
