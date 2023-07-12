import pygame
import random
from settings import *
from sprites import * 

class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.obs = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.obs, False)
            if hits:
                self.playing = False
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw(self):
        self.screen.fill(white)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()