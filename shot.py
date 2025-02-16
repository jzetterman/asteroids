import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        
        # Automatically add the instance to groups in the 'containers' variable
        if hasattr(self.__class__, 'containers'):  # Check if 'containers' is defined
            for group in self.__class__.containers:  # Loop over the groups
                group.add(self)  # Add 'self' to each group

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt