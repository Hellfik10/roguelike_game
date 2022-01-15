import pygame

import sprite_groups
from load import load_image


class HP(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(HP, self).__init__()
        self.image = load_image('door.jpeg')
        self.rect = self.image.get_rect()
        self.rect.centerx = coords[0]
        self.rect.centery = coords[1]

    def update(self):
        if pygame.sprite.spritecollideany(self, sprite_groups.player_group):
            for sprite in sprite_groups.player_group:
                sprite.HP += 1
                print(sprite.HP)
            sprite_groups.bonus_group.empty()


class FastMove(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(FastMove, self).__init__()
        self.image = load_image('door.jpeg')
        self.rect = self.image.get_rect()
        self.rect.centerx = coords[0]
        self.rect.centery = coords[1]

    def update(self):
        if pygame.sprite.spritecollideany(self, sprite_groups.player_group):
            for sprite in sprite_groups.player_group:
                sprite.v += 1
                print(sprite.v)
            sprite_groups.bonus_group.empty()
