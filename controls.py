import pygame, sys
from pygame.sprite import Group
from bullets import Bullet
v = 2


def events(screen, player, bullets, w, h):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Перемещение
        if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_w]:
            player.rect.centerx += v
            player.rect.centery -= v
            player.side = 'right'
        if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_s]:
            player.rect.centerx += v
            player.rect.centery += v
            player.side = 'right'
        if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_w]:
            player.rect.centerx -= v
            player.rect.centery -= v
            player.side = 'left'
        if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_s]:
            player.rect.centerx -= v
            player.rect.centery += v
            player.side = 'left'
        if pygame.key.get_pressed()[pygame.K_d]:
            player.rect.centerx += v
            player.side = 'right'
        if pygame.key.get_pressed()[pygame.K_a]:
            player.rect.centerx -= v
            player.side = 'left'
        if pygame.key.get_pressed()[pygame.K_w]:
            player.rect.centery -= v
            player.side = 'top'
        if pygame.key.get_pressed()[pygame.K_s]:
            player.rect.centery += v
            player.side = 'bottom'

        # Атака
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet(screen, player, event.pos[0], event.pos[1])
            bullets.add(new_bullet)


def update_bullets(enemys, bullets, w, h):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.x < 0 or bullet.rect.x > w - 50 or bullet.rect.y < 0 or bullet.rect.y > h - 50:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)
