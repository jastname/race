import pygame 
from settings import *
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((30, 40))
        self.image.fill(orange)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        self.rect.y -= 0.1
        if self.pos.y == 680:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x*PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > 640:
            self.pos.y = 640

        self.rect.midbottom = self.pos

class obs(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
