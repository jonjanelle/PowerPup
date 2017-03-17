import pygame, bullet
pygame.init()
class Player:
    def __init__(self,x,y,dx,dy,color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.img = pygame.image.load("player.png").convert()
        self.img.set_colorkey((255,255,255))
        self.img = pygame.transform.scale(self.img,(60,45))
        self.dir = 'r'
        self.health = 3
        self.bullets = []
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def draw(self,screen):
        #Draw self
        screen.blit(self.img,(self.x,self.y))
        #Draw projectiles
        for b in self.bullets:
            b.draw(screen)
            
            
    def flip_img(self, direction):
        if self.dir == 'l' and direction == 'r':
            self.dir = 'r'
            self.img = pygame.transform.flip(self.img,True,False)
        elif self.dir == 'r' and direction == 'l':
            self.dir = 'l'
            self.img = pygame.transform.flip(self.img,True,False)

    def move(self):
        mb = pygame.mouse.get_pressed()
        if 1 in mb:
            pos = pygame.mouse.get_pos()
            if pos[0]-self.x > 0 and abs(pos[0]-self.x) > self.img.get_width():
                self.x += self.dx
                self.flip_img('r')
            elif self.dir == 'l' and pos[0]-self.x < 0:
                self.x -= self.dx
                self.flip_img('l')
                    
            if abs(pos[1]-self.y) > self.img.get_height():
                if pos[1]-self.y > 0:
                    self.y += self.dy
                else:
                    self.y -= self.dy
        else:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.flip_img('l')
                self.x -= self.dx
            elif pressed[pygame.K_RIGHT]:
                self.flip_img('r')
                self.x += self.dx
            if pressed[pygame.K_UP]:
                self.y -= self.dy
            elif pressed[pygame.K_DOWN]:
                self.y += self.dy
                

    def collideball(self, ball):
        brect = pygame.Rect(ball.x-ball.size, ball.y-ball.size,2*ball.size,2*ball.size)
        if brect.colliderect(self.get_rect()):
            self.health -= 1
            return True
        else:
            return False

    def shoot(self):
        if self.dir == 'r':
            dx = 10
            x = self.x + 30
        else:
            dx = -10
            x = self.x - 30
            
        #bullet = Bullet(x,self.y, dx, 0)
        #self.bullets.append(bullet)
            
