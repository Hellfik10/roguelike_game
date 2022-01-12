import pygame
from load import load_image
v = 2

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.image = load_image('mario.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def output(self):
        self.screen.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, spawn):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = load_image('bad_mario.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = spawn[0]
        self.rect.centery = spawn[1]

    def output(self):
        self.screen.blit(self.image, self.rect)

    def action(self, player):
        if abs(self.rect.centerx - player.rect.centerx) < 50 and abs(self.rect.centery - player.rect.centery) < 50:
            if self.rect.centerx < player.rect.centerx:
                self.rect.centerx -= v
            else:
                self.rect.centerx += v
            if self.rect.centery < player.rect.centery:
                self.rect.centery -= v
            else:
                self.rect.centery += v