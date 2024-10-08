import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass

    def detect_collision(self, circleShape):
        distance = self.position.distance_to(circleShape.position)
        radius_sum = self.radius + circleShape.radius
        return (distance <= radius_sum)
