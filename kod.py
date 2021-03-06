import sys
import pygame
import map
import creatures
import sprite_groups
import controls
import door
from interface import Interface
from load import load_image


def terminate():
    pygame.quit()
    sys.exit()


size = width, height = 800, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption('roguelike_game')

FPS = 60
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 3000)

map = map.Map(width, height, screen)

player = creatures.Player(screen)
sprite_groups.player_group.add(player)

door = door.Door(screen)
timer_for_ammos = 0

i = Interface()

while True:
    controls.events(screen, player)
    controls.update_enemys(sprite_groups.enemys, player)
    sprite_groups.all_sprites.draw(screen)
    screen.blit(map.fon_get()[0], map.fon_get()[1])
    sprite_groups.bonus_group.draw(screen)
    sprite_groups.environment_group.draw(screen)
    screen.blit(load_image('health_bar.png'), (0, 0))
    screen.blit(i.output(player.HP, map.lvl, map.room, player.ammos)[0], (50, 0))
    screen.blit(i.output(player.HP, map.lvl, map.room, player.ammos)[1],
                (i.output(player.HP, map.lvl, map.room, player.ammos)[2], 0))
    screen.blit(i.output(player.HP, map.lvl, map.room, player.ammos)[3], (750, 550))
    controls.update_bullets(sprite_groups.enemys, sprite_groups.players_bullets, width, height)
    controls.update_bullets(sprite_groups.player_group, sprite_groups.enemys_bullets, width, height, False)
    controls.update_bullets(sprite_groups.environment_group, sprite_groups.players_bullets, width, height)
    controls.update_bullets(sprite_groups.environment_group, sprite_groups.enemys_bullets, width, height)
    player.update_moving()
    sprite_groups.players_bullets.draw(screen)
    sprite_groups.enemys_bullets.draw(screen)
    sprite_groups.enemys.update()
    sprite_groups.enemys.draw(screen)
    player.output()
    map.next_room(door.update(map.door_state_get(), map))
    player.update()
    sprite_groups.bonus_group.update()
    if player.ammos == 0:
        timer_for_ammos += 1
        if timer_for_ammos == 100:
            timer_for_ammos = 0
            player.ammos += player.max_ammos

    pygame.display.flip()
    clock.tick(FPS)