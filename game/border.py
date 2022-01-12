import pygame


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super(Border, self).__init__()
        if x1 == x2:
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)