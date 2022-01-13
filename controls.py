import pygame, sys
from pygame.sprite import Group
from bullets import Bullet
import sprite_groups

v = 5


def events(screen, player, p, bullets, w, h):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Перемещение
        if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_w] and 2 not in p and 3 not in p:
            player.rect.centerx += v ** 0.5
            player.rect.centery -= v ** 0.5
            player.side = 'right'
        if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_s] and 2 not in p and 4 not in p:
            player.rect.centerx += v ** 0.5
            player.rect.centery += v ** 0.5
            player.side = 'right'
        if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_w] and 3 not in p and 1 not in p:
            player.rect.centerx -= v ** 0.5
            player.rect.centery -= v ** 0.5
            player.side = 'left'
        if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_s] and 4 not in p and 1 not in p:
            player.rect.centerx -= v ** 0.5
            player.rect.centery += v ** 0.5
            player.side = 'left'
        if pygame.key.get_pressed()[pygame.K_d] and 2 not in p:
            player.rect.centerx += v
            player.side = 'right'
        if pygame.key.get_pressed()[pygame.K_a] and 1 not in p:
            player.rect.centerx -= v
            player.side = 'left'
        if pygame.key.get_pressed()[pygame.K_w] and 3 not in p:
            player.rect.centery -= v
            player.side = 'top'
        if pygame.key.get_pressed()[pygame.K_s] and 4 not in p:
            player.rect.centery += v
            player.side = 'bottom'

        # Атака
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet(screen, player, event.pos[0], event.pos[1])
            sprite_groups.bullets.add(new_bullet)


def update_bullets(enemys, bullets, w, h):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.x < 50 or bullet.rect.x > w - 50 or bullet.rect.y < 50 or bullet.rect.y > h - 50:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)


def update_enemys(enemys, player):
    for enemy in enemys.copy():
        if abs(enemy.rect.centerx - player.rect.centerx) < 200 and abs(enemy.rect.centery - player.rect.centery) < 170:
            enemy.moving_away(player, False)
        else:
            enemy.moving_away(player, True)
        for enemy2 in enemys.copy():
            if abs(enemy.rect.centerx - enemy2.rect.centerx) < 100 and abs(
                    enemy.rect.centery - enemy2.rect.centery) < 100:
                enemy.moving_away(enemy2, False)
