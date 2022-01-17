import pygame

import sprite_groups
from load import load_image


# Улучшения для игрока (дополнительная жизнь, ускорение перемещения, усиление и ускорение пули игрока)


class HP(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(HP, self).__init__()
        self.image = pygame.transform.scale(load_image('prizehe.png'), (50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = coords[0]
        self.rect.centery = coords[1]

    def update(self):
        if pygame.sprite.spritecollideany(self, sprite_groups.player_group):
            for sprite in sprite_groups.player_group:
                if sprite.HP != 100:
                    sprite.HP += 1
            sprite_groups.bonus_group.empty()


class FastMovePlayer(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(FastMovePlayer, self).__init__()
        self.image = pygame.transform.scale(load_image('prizesapog.png'), (50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = coords[0]
        self.rect.centery = coords[1]

    def update(self):
        if pygame.sprite.spritecollideany(self, sprite_groups.player_group):
            for sprite in sprite_groups.player_group:
                if sprite.v != 40:
                    sprite.v += 1
            sprite_groups.bonus_group.empty()


class FastMoveBulletsPlayer(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(FastMoveBulletsPlayer, self).__init__()
        self.image = pygame.transform.scale(load_image('prizespeed.png'), (50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = coords[0]
        self.rect.centery = coords[1]

    def update(self):
        if pygame.sprite.spritecollideany(self, sprite_groups.player_group):
            for sprite in sprite_groups.player_group:
                if sprite.multiplier != 30:
                    sprite.multiplier += 1
            sprite_groups.bonus_group.empty()


class MoreStrongerBulletsPlayer(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(MoreStrongerBulletsPlayer, self).__init__()
        self.image = pygame.transform.scale(load_image('prizestr.png'), (50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = coords[0]
        self.rect.centery = coords[1]

    def update(self):
        if pygame.sprite.spritecollideany(self, sprite_groups.player_group):
            for sprite in sprite_groups.player_group:
                sprite.damage += 1
            sprite_groups.bonus_group.empty()