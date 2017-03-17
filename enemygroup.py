import pygame, random, math,ball

class EnemyGroup:
    def __init__(self, dim):
        self.W = dim[0]
        self.H = dim[1]
        self.enemies = list()
        
    def make_enemies(self, count, minfac, maxfac):
        self.enemies = []
        dirs = [-1,1]
        for i in range(count):
            x = (random.randint(100, self.W-50))
            y = (random.randint(100, self.H-50))
            color = (random.randint(100, 255),random.randint(100, 255),random.randint(100, 255))
            speed = random.randint(minfac,maxfac)/(12000.0+300*maxfac)*dirs[random.randint(0,1)]
            
            size = random.randint(8,30)
            new_enemy = ball.Ball(x,y,speed,size,color)
            self.enemies.append(new_enemy)

    def move(self,p1):
        #Move all and check for collisions
        for b1 in self.enemies:
            #check for collisions with player
            if p1.collideball(b1):
                self.enemies.remove(b1)
                continue
            for b2 in self.enemies:
                if b1 != b2:
                    b2.move(b1.x, b1.y)
                    b1.checkcollide(b2)

    def draw(self,screen):
        for b in self.enemies:
            b.draw(screen)
