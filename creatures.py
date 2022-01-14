import pygame

import bullets
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

    def shooting(self, player):
        if ((self.rect.centery - player.rect.centery) ** 2 + (
                self.rect.centerx - player.rect.centerx) ** 2) ** 0.5 > 125:
            new_bullet = bullets.Enemy_bullet(self.screen, self, player.rect.centerx, player.rect.centery)
            sprite_groups.enemys_bullets.add(new_bullet)
            print(len((sprite_groups.enemys_bullets)))
