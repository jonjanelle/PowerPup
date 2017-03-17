import pygame, random
class Trail:
    def __init__(self,length):
        self.length = length
        self.points = []
        self.size = 5
        self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        
    def add(self, point):
        self.points.append(point)
        if len(self.points) > self.length:
            self.points.pop(0)
    
    def draw(self, screen):
        for p in self.points:
            pygame.draw.circle(screen, self.color, p, self.size)
            pygame.draw.circle(screen, (120,200,120), p, self.size,1)
        
