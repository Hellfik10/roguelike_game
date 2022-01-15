import pygame
from load import load_image


class HP(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(HP, self).__init__()
        self.image = load_image('HP.jpeg')
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery =  0