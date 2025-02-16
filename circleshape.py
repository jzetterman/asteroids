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
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, circle):
        distance = self.radius + circle.radius
        print(f"Distance: {distance}, Distance_To: {circle.position.distance_to(self.position)}")

        if circle.position.distance_to(self.position) <= distance:
            return True
        else:
            return False