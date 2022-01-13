import sprite_groups
import pygame
from load import load_image


class Door(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        super(Door, self).__init__()
        self.image = pygame.Surface([60, 15])
        self.rect = pygame.Rect(370, 50, 60, 15)

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self, door_state, map):
        if pygame.sprite.spritecollideany(self, sprite_groups.player_group) and door_state:
            return True
