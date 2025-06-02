from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        angle = random.uniform(20,50)
        vector1_veloctiy = pygame.math.Vector2.rotate(self.velocity, angle)
        vector2_veloctiy = pygame.math.Vector2.rotate(self.velocity, -1 * angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = vector1_veloctiy * 1.2
        asteroid_2.velocity = vector2_veloctiy * 1.2

        

        
