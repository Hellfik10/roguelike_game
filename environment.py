import pygame
from load import load_image


class Box(pygame.sprite.Sprite):
    def __init__(self, spawn):
        super(Box, self).__init__()
        self.image = pygame.transform.scale(load_image('door.png'), (50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn[0] + 50 + (self.rect.right - self.rect.left) // 2
        self.rect.centery = spawn[1] + 50 + (self.rect.bottom - self.rect.top) // 2
