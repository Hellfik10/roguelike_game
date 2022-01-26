import pygame, sys
from pygame.sprite import Group
from bullets import Player_bullet
import sprite_groups

v = 5


def events(screen, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT:
            for enemy in sprite_groups.enemys.copy():
                enemy.shooting(player)

        # Перемещение игрока
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.mright = True
                player.side = 'right'
                player.knopka = True
            if event.key == pygame.K_a:
                player.mleft = True
                player.side = 'left'
                player.knopka = False
            if event.key == pygame.K_w:
                player.mup = True
                player.side = 'top'
            if event.key == pygame.K_s:
                player.mdown = True
                player.side = 'bottom'
            if event.key == pygame.K_r:
                player.ammos = 0
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
                if player.ammos > 0:
                    for sprite in sprite_groups.player_group:
                        multiplier = sprite.multiplier
                    new_bullet = Player_bullet(screen, player, event.pos[0], event.pos[1], multiplier)
                    sprite_groups.players_bullets.add(new_bullet)
                    player.is_shooting = True
                    player.ammos -= 1


def update_bullets(enemys, bullets, w, h):
    # Обновление пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.x < 50 or bullet.rect.right > w - 50 or bullet.rect.y < 50 or bullet.rect.bottom > h - 50:
            bullets.remove(bullet)
    if enemys == sprite_groups.player_group:
        collisions = pygame.sprite.groupcollide(bullets, enemys, True, False)
        for player in enemys:
            player.HP -= len(collisions)
            if player.HP < 1:
                player.game_over = True
    elif enemys == sprite_groups.environment_group:
        pygame.sprite.groupcollide(enemys, bullets, True, True)
    else:
        for sprite in sprite_groups.player_group:
            damage = sprite.damage
            break
        for enemy in enemys:
            collisions = pygame.sprite.spritecollide(enemy, bullets, True)
            enemy.HP -= len(collisions) * damage
            if enemy.HP < 1:
                enemy.kill()


def update_enemys(enemys, player):
    #Перемещениие врагов
    for enemy in enemys.copy():
        if abs(enemy.rect.centerx - player.rect.centerx) < 250 and abs(enemy.rect.centery - player.rect.centery) < 200:
            enemy.moving_away(player, False)
        else:
            enemy.moving_away(player, True)
        for enemy2 in enemys.copy():
            if abs(enemy.rect.centerx - enemy2.rect.centerx) < 100 and abs(
                    enemy.rect.centery - enemy2.rect.centery) < 100:
                enemy.moving_away(enemy2, False)
