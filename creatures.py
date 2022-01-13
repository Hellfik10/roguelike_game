import pygame
from load import load_image
import sprite_groups

v = 1


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

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        sp = []
        if pygame.sprite.spritecollideany(self, sprite_groups.left):
            sp.append(1)
        if pygame.sprite.spritecollideany(self, sprite_groups.right):
            sp.append(2)
        if pygame.sprite.spritecollideany(self, sprite_groups.top):
            sp.append(3)
        if pygame.sprite.spritecollideany(self, sprite_groups.bottom):
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

    def moving_away(self, player, hunting):
        if hunting:
            if self.rect.centerx < player.rect.centerx:
                self.rect.centerx += v
            else:
                self.rect.centerx -= v
            if self.rect.centery < player.rect.centery:
                self.rect.centery += v
            else:
                self.rect.centery -= v
        else:
            if 75 < self.rect.centerx < player.rect.centerx:
                self.rect.centerx -= v
            elif 730 > self.rect.centerx > player.rect.centerx:
                self.rect.centerx += v
            if 75 < self.rect.centery < player.rect.centery:
                self.rect.centery -= v
            elif 530 > self.rect.centery > player.rect.centery:

                self.rect.centery += v
