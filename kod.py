import sys
import pygame
import controls, door, sprite_groups, creatures, load
from map import Map
from interface import Interface
from menu import Menu


def terminate():
    pygame.quit()
    sys.exit()


size = width, height = 800, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption('roguelike_game')

FPS = 60
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 3000)

map = Map(width, height, screen)
menu = Menu()
menu.append_option('Играть', 'play')
menu.append_option('Выход', 'exit')
menu_running = True

go_menu = Menu()
go_menu.append_option('Играть заново', 'play')
go_menu.append_option('Выход', 'exit')

player = creatures.Player(screen)
sprite_groups.player_group.add(player)

door = door.Door(screen)
timer_for_ammos = 0

i = Interface()

while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                menu.switch(-1)
            elif event.key == pygame.K_s:
                menu.switch(1)
            elif event.key == pygame.K_UP:
                menu.switch(-1)
            elif event.key == pygame.K_DOWN:
                menu.switch(1)
            elif event.key == pygame.K_RETURN:
                if menu.select() == 'play':
                    menu_running = False
                else:
                    sys.exit()
    screen.blit(load.load_image('fon_open_door.png'), (0, 0))
    menu.draw(screen, 100, 200, 75)
    pygame.display.flip()

while True:
    if not player.game_over:
        controls.events(screen, player)
        controls.update_enemys(sprite_groups.enemys, player)
        sprite_groups.all_sprites.draw(screen)
        screen.blit(map.fon_get()[0], map.fon_get()[1])
        sprite_groups.bonus_group.draw(screen)
        sprite_groups.environment_group.draw(screen)
        screen.blit(load.load_image('health_bar.png'), (0, 0))
        screen.blit(i.output(player.HP, map.lvl, map.room, player.ammos)[0], (50, 0))
        screen.blit(i.output(player.HP, map.lvl, map.room, player.ammos)[1],
                    (i.output(player.HP, map.lvl, map.room, player.ammos)[2], 0))
        screen.blit(i.output(player.HP, map.lvl, map.room, player.ammos)[3], (750, 550))
        controls.update_bullets(sprite_groups.enemys, sprite_groups.players_bullets, width, height)
        controls.update_bullets(sprite_groups.player_group, sprite_groups.enemys_bullets, width, height)
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
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    go_menu.switch(-1)
                elif event.key == pygame.K_s:
                    go_menu.switch(1)
                elif event.key == pygame.K_UP:
                    go_menu.switch(-1)
                elif event.key == pygame.K_DOWN:
                    go_menu.switch(1)
                elif event.key == pygame.K_RETURN:
                    if go_menu.select() == 'play':
                        i = Interface()
                        player = creatures.Player(screen)
                        map = Map(width, height, screen)

                        sprite_groups.all_sprites = pygame.sprite.Group()
                        sprite_groups.tiles_group = pygame.sprite.Group()

                        sprite_groups.player_group = pygame.sprite.Group()
                        sprite_groups.players_bullets = pygame.sprite.Group()
                        sprite_groups.enemys = pygame.sprite.Group()
                        sprite_groups.enemys_bullets = pygame.sprite.Group()

                        sprite_groups.door_group = pygame.sprite.Group()

                        sprite_groups.bonus_group = pygame.sprite.Group()
                        sprite_groups.environment_group = pygame.sprite.Group()

                        sprite_groups.player_group.add(player)

                    else:
                        sys.exit()
        screen.blit(load.load_image('fon_open_door.png'), (0, 0))
        go_menu.draw(screen, 100, 200, 75)

    pygame.display.flip()
    clock.tick(FPS)
