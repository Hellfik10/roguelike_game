import sys
import pygame
import map
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

map = map.Map(width, height, screen)

player = creatures.Player(screen)
sprite_groups.player_group.add(player)

door = door.Door(screen)

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
    door.output()

    pygame.display.flip()
    clock.tick(FPS)
