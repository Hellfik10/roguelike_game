import pygame, sys
from pygame.sprite import Group
from bullets import Player_bullet
import sprite_groups

v = 5


def events(screen, player, enemys):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT:
            for enemy in sprite_groups.enemys.copy():
                enemy.shooting(player)

        # Перемещение
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.mright = True
                player.side = 'right'
            if event.key == pygame.K_a:
                player.mleft = True
                player.side = 'left'
            if event.key == pygame.K_w:
                player.mup = True
                player.side = 'top'
            if event.key == pygame.K_s:
                player.mdown = True
                player.side = 'bottom'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.mright = False
            if event.key == pygame.K_a:
                player.mleft = False
            if event.key == pygame.K_w:
                player.mup = False
            if event.key == pygame.K_s:
                player.mdown = False

        # Атака
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_bullet = Player_bullet(screen, player, event.pos[0], event.pos[1])
                sprite_groups.players_bullets.add(new_bullet)


def update_bullets(enemys, bullets, w, h, lives=True):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.x < 50 or bullet.rect.right > w - 50 or bullet.rect.y < 50 or bullet.rect.bottom > h - 50:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemys, True, lives)


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
