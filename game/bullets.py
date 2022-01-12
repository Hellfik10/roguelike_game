import pygame
from load import load_image


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, creature, click_x, click_y):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = load_image('bullet.png')
        self.pos = pygame.math.Vector2(creature.rect.centerx, creature.rect.centery)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = creature.rect.centerx
        self.rect.centery = creature.rect.centery
        self.vector = pygame.math.Vector2
        self.dir = pygame.math.Vector2(click_x - self.rect.centerx, click_y - self.rect.centery).normalize()

    def update(self):
        self.pos += self.dir * 5
        self.rect.center = round(self.pos.x), round(self.pos.y)

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)