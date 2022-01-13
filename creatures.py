import pygame
from load import load_image
import sprite_groups


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.add(sprite_groups.all_sprites)
        self.screen = screen
        self.image = load_image('mario.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def player_pos(self, pos):
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        sp = []
        if self.rect.left <= 50:
            sp.append(1)
        if self.rect.right >= 750:
            sp.append(2)
        if self.rect.top <= 50:
            sp.append(3)
        if  self.rect.bottom >= 550:
            sp.append(4)
        return sp


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