import pygame

import bullets
from load import load_image
import sprite_groups
from controls import events

v = 2


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.knopka = None
        self.add(sprite_groups.all_sprites)
        self.cur_frame = 0
        self.screen = screen
        if self.knopka:
            self.image = pygame.transform.scale(load_image('va2.png'), (58, 62))
        else:
            self.image = pygame.transform.scale(load_image('val2.png'), (58, 62))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False
        self.animCount = 0
        self.v = 5
        self.walkRight = [pygame.transform.scale(load_image('vr1.png'), (58, 62)),
                          pygame.transform.scale(load_image('vr2.png'), (67, 62)),
                          pygame.transform.scale(load_image('vr3.png'), (58, 57))]
        self.afkr = [pygame.transform.scale(load_image('va2.png'), (48, 62))]
        self.afkl = [pygame.transform.scale(load_image('val2.png'), (48, 62))]
        self.walkLeft = [pygame.transform.scale(load_image('vl1.png'), (58, 62)),
                         pygame.transform.scale(load_image('vl2.png'), (67, 62)),
                         pygame.transform.scale(load_image('vl3.png'), (58, 57))]
        self.shooting_sprites_right = [pygame.transform.scale(load_image('players_slash\\vs1.png'), (48, 62)),
                                 pygame.transform.scale(load_image('players_slash\\vs3.png'), (53, 62)),
                                 pygame.transform.scale(load_image('players_slash\\vs4.png'), (62, 62)),
                                 pygame.transform.scale(load_image('players_slash\\vs5.png'), (72, 62)),
                                 pygame.transform.scale(load_image('players_slash\\vs6.png'), (48, 62))]
        self.shooting_sprites_left = [pygame.transform.scale(load_image('players_slash\\vq1.png'), (48, 62)),
                                       pygame.transform.scale(load_image('players_slash\\vq3.png'), (53, 62)),
                                       pygame.transform.scale(load_image('players_slash\\vq4.png'), (62, 62)),
                                       pygame.transform.scale(load_image('players_slash\\vq5.png'), (72, 62)),
                                       pygame.transform.scale(load_image('players_slash\\vq6.png'), (48, 62))]
        self.is_shooting = False
        self.timer_for_shooting = 0
        self.timer = 0
        self.timer1 = 0
        self.HP = 100000
        self.multiplier = 5

    def player_pos(self, pos):
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def output(self):
        self.screen.blit(self.image, self.rect)

    def possibility_of_movement(self):
        sp = []
        if self.rect.left <= 50:
            sp.append('block left')
        if self.rect.right >= 760:
            sp.append('block right')
        if self.rect.top <= 50:
            sp.append('block up')
        if self.rect.bottom >= 550:
            sp.append('block down')
        return sp

    def update_moving(self):
        if self.mright and 'block right' not in self.possibility_of_movement():
            self.rect.centerx += self.v
            if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                self.rect.centerx -= self.v
        if self.mleft and 'block left' not in self.possibility_of_movement():
            self.rect.centerx -= self.v
            if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                self.rect.centerx += self.v
        if self.mup and 'block up' not in self.possibility_of_movement():
            self.rect.centery -= self.v
            if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                self.rect.centery += self.v
        if self.mdown and 'block down' not in self.possibility_of_movement():
            self.rect.centery += self.v
            if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                self.rect.centery -= self.v
        if self.rect.left < 50:
            self.rect.centerx = 50 + (self.rect.right - self.rect.left) // 2
        if self.rect.top < 50:
            self.rect.centery = 50 + (self.rect.bottom - self.rect.top) // 2
        if self.rect.right > 760:
            self.rect.centerx = 760 - (self.rect.right - self.rect.left) // 2
        if self.rect.bottom > 550:
            self.rect.centery = 550 - (self.rect.bottom - self.rect.top) // 2

    def update(self):
        if self.is_shooting and self.knopka:
            self.timer_for_shooting += 1
            if self.timer_for_shooting == 5:
                self.timer_for_shooting = 0
                self.cur_frame = (self.cur_frame + 1) % len(self.shooting_sprites_right)
                self.image = self.shooting_sprites_right[self.cur_frame]
            if self.cur_frame == 3:
                self.is_shooting = False
        elif self.is_shooting and not(self.knopka):
            self.timer_for_shooting += 1
            if self.timer_for_shooting == 5:
                self.timer_for_shooting = 0
                self.cur_frame = (self.cur_frame + 1) % len(self.shooting_sprites_left)
                self.image = self.shooting_sprites_left[self.cur_frame]
            if self.cur_frame == 3:
                self.is_shooting = False
        else:
            if self.mright and 'block right' not in self.possibility_of_movement():
                self.timer += 1
                if self.timer == 5:
                    self.timer = 0
                    self.cur_frame = (self.cur_frame + 1) % len(self.walkRight)
                    self.image = self.walkRight[self.cur_frame]
            elif self.mleft and 'block left' not in self.possibility_of_movement():
                self.timer += 1
                if self.timer == 5:
                    self.timer = 0
                    self.cur_frame = (self.cur_frame + 1) % len(self.walkLeft)
                    self.image = self.walkLeft[self.cur_frame]
            elif self.mup and 'block up' not in self.possibility_of_movement():
                if self.knopka:
                    self.timer += 1
                    if self.timer == 5:
                        self.timer = 0
                        self.cur_frame = (self.cur_frame + 1) % len(self.walkRight)
                        self.image = self.walkRight[self.cur_frame]
                else:
                    self.timer += 1
                    if self.timer == 5:
                        self.timer = 0
                        self.cur_frame = (self.cur_frame + 1) % len(self.walkLeft)
                        self.image = self.walkLeft[self.cur_frame]
            elif self.mdown and 'block down' not in self.possibility_of_movement():
                if self.knopka:
                    self.timer += 1
                    if self.timer == 5:
                        self.timer = 0
                        self.cur_frame = (self.cur_frame + 1) % len(self.walkRight)
                        self.image = self.walkRight[self.cur_frame]
                else:
                    self.timer += 1
                    if self.timer == 5:
                        self.timer = 0
                        self.cur_frame = (self.cur_frame + 1) % len(self.walkLeft)
                        self.image = self.walkLeft[self.cur_frame]
            else:
                if self.knopka:
                    self.timer1 = 0
                    self.cur_frame = (self.cur_frame + 1) % len(self.afkr)
                    self.image = self.afkr[self.cur_frame]
                else:
                    self.timer1 = 0
                    self.cur_frame = (self.cur_frame + 1) % len(self.afkl)
                    self.image = self.afkl[self.cur_frame]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, spawn, HP):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.transform.scale(load_image('el1.png'), (69.5,58))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = spawn[0] + 50 + (self.rect.right - self.rect.left) // 2
        self.rect.centery = spawn[1] + 50 + (self.rect.bottom - self.rect.top) // 2
        self.HP = HP
        self.cur_frame = 0
        self.timer = 0
        self.anime = [pygame.transform.scale(load_image('el1.png'), (93,77)),
                      pygame.transform.scale(load_image('el2.png'), (91, 65)),
                      pygame.transform.scale(load_image('el3.png'), (94, 67)),
                      pygame.transform.scale(load_image('el4.png'), (72, 64))]

    def update(self):
        self.timer += 1
        if self.timer == 10:
            self.timer = 0
            self.cur_frame = (self.cur_frame + 1) % len(self.anime)
            self.image = self.anime[self.cur_frame]

    def moving_away(self, player, hunting):
        if hunting:
            if self.rect.centerx < player.rect.centerx:
                self.rect.centerx += v
                if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                    self.rect.centerx -= v
            else:
                self.rect.centerx -= v
                if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                    self.rect.centerx += v
            if self.rect.centery < player.rect.centery:
                self.rect.centery += v
                if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                    self.rect.centery -= v
            else:
                self.rect.centery -= v
                if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                    self.rect.centery += v
        else:
            if 75 < self.rect.centerx < player.rect.centerx:
                self.rect.centerx -= v
                if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                    self.rect.centerx += v
            elif 730 > self.rect.centerx > player.rect.centerx:
                self.rect.centerx += v
                if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                    self.rect.centerx -= v
            if 75 < self.rect.centery < player.rect.centery:
                self.rect.centery -= v
                if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                    self.rect.centery += v
            elif 530 > self.rect.centery > player.rect.centery:
                self.rect.centery += v
                if pygame.sprite.spritecollideany(self, sprite_groups.environment_group):
                    self.rect.centery -= v

    def shooting(self, player):
        if ((self.rect.centery - player.rect.centery) ** 2 + (
                self.rect.centerx - player.rect.centerx) ** 2) ** 0.5 > 125:
            new_bullet = bullets.Enemy_bullet(self.screen, self, player.rect.centerx, player.rect.centery)
            sprite_groups.enemys_bullets.add(new_bullet)
