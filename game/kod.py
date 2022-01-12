import sys
import pygame
import map
from border import Border
import creatures
import sprite_groups
import controls
import bullets
import door

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption('roguelike_game')

FPS = 60
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


map = map.Map(width, height, screen)

player = creatures.Player(screen)
sprite_groups.player_group.add(player)

border1 = Border(50, 50, 750, 50)
sprite_groups.top.add(border1)
border2 = Border(50, 50, 50, 550)
sprite_groups.left.add(border2)
border3 = Border(50, 550, 750, 550)
sprite_groups.bottom.add(border3)
border4 = Border(750, 50, 750, 550)
sprite_groups.right.add(border4)

door = door.Door()

while True:
    controls.events(screen, player, player.update(), bullets, width, height)
    screen.fill('black')
    sprite_groups.all_sprites.draw(screen)
    screen.blit(map.fon_get()[0], map.fon_get()[1])
    controls.update_bullets(sprite_groups.enemys, sprite_groups.bullets, width, height)
    sprite_groups.bullets.draw(screen)
    sprite_groups.enemys.draw(screen)
    player.output()
    map.next_room(door.update(map.door_state_get(), map))

    pygame.display.flip()
    clock.tick(FPS)
