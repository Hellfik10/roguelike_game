import pygame
import sys
import creatures, controls, bullets
from pygame.sprite import Group


def terminate():
    pygame.quit()
    sys.exit()


# основной персонаж
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перемещение героя')

    size = WIDTH, HEIGHT = 800, 600
    FPS = 50
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    clock = pygame.time.Clock()

    player = creatures.Player(screen)
    bullets = Group()
    enemys = Group()
    v = 1.5

    new_enemy = creatures.Enemy(screen, [200, 200])
    enemys.add(new_enemy)

    while True:
        controls.events(screen, player, bullets, WIDTH, HEIGHT)
        screen.fill('black')
        controls.update_bullets(enemys, bullets, WIDTH, HEIGHT)
        controls.update_enemy(enemys, player)
        bullets.draw(screen)
        enemys.draw(screen)
        player.output()

        clock.tick(FPS)
        pygame.display.flip()
