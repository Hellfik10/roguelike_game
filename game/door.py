import sprite_groups
import pygame
from load import load_image


class Door(pygame.sprite.Sprite):
    def __init__(self):
        super(Door, self).__init__()
        self.image = load_image('door.jpeg')
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 25

    def update(self, door_state, map):
        if pygame.sprite.spritecollideany(self, sprite_groups.player_group) and door_state:
            return True
