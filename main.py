import pygame

class BaseSprite:
    def __init__(self, x, y, texture,speed, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)



class Hero(BaseSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed

class Wall:
    def __init__(self, x, y, color, w, h):
        self.hitbox = pygame.Rect(x, y, w, h)
        self.hitbox.x = x
        self.hitbox.y = y
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

pygame.init()

window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()

background_img = pygame.image.load("background2.png.")
background_img = pygame.transform.scale(background_img, [700, 500])
hero = Hero(250, 250, "hero.png", 2, 50, 50)

walls = [
    Wall(160, 187, [250, 0, 0], 20, 100),
    Wall(160, 372, [250, 0, 0], 100, 20)
]


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    hero.update()

    window.fill([104, 1, 14])
    window.blit(background_img, [0, 0])
    hero.draw(window)
    for wall in walls:
        wall.draw(window)
    pygame.display.flip()


    clock.tick(60)


