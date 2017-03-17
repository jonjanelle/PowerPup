import pygame, math, random
from trail import Trail
class Ball:
    def __init__(self, startx, starty, angleSpeed, size, color):
        self.x = startx
        self.y = starty
        self.startx = startx
        self.starty = starty
        self.speed = angleSpeed
        self.size = size
        self.color = color
        self.angle_move=0
        self.trail = Trail(random.randint(15,35))

    def move(self, centerx, centery):
        #Centerx is the x center of rotation
        #Centery is the y center of rotation
        dx = self.x - centerx #x dist from self to center
        dy = self.y - centery #y dist from self to center
        r = math.sqrt(dx**2+dy**2) #radius of rotation
        angle = math.atan2(dy,dx) #angle between self and center

        angle = angle + self.speed #Adjust angle by speed to move
        #Update x and y positions
        self.x = int(round(r*math.cos(angle),0))+centerx#convert back to rectangular
        self.y = int(round(r*math.sin(angle),0))+centery#convert back to rectangular

    def dist(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**.5
    
    def checkcollide(self, other):      
        if self.dist(other) < self.size+other.size:
            self.speed *= -1
            other.speed *= -1
            randx = random.randint(-8,8)
            randy = random.randint(-8,8)
            self.x += randx
            self.y += randy
            other.x -= randx
            other.y -= randy
            
        else:
            return False
        
    def draw(self, screen):
        self.trail.add((self.x,self.y))
        self.trail.draw(screen)
        pygame.draw.circle(screen, self.color, (self.x, self.y),self.size)
        #pygame.draw.circle(screen, (0,0,0), (self.x, self.y),self.size,2)
     
