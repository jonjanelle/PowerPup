class Bullet:
    def __init__(self, x, y, dx, dy, img = "fireball.png"):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.img = pygame.image.load(img).convert()

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        self.x += self.dx
        self.y += self.dy

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
    

