import pygame

import bullets
from load import load_image
import sprite_groups

v = 2


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.add(sprite_groups.all_sprites)
        self.cur_frame = 0
        self.screen = screen
        self.image = load_image('va2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False
        self.animCount = 0
        self.velocity = 5
        self.walkRight = [load_image('vr1.png'), load_image('vr2.png'),
                          load_image('vr3.png')]
        self.afk = [load_image('va2.png')]
        self.walkLeft = [load_image('vl1.png'), load_image('vl2.png'),
                          load_image('vl3.png')]
        self.timer = 0
        self.timer1 = 0

    def player_pos(self, pos):
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def output(self):
        self.screen.blit(self.image, self.rect)

    def possibility_of_movement(self):
        sp = []
        if self.rect.left <= 50:
            sp.append('block left')
        if self.rect.right >= 750:
            sp.append('block right')
        if self.rect.top <= 50:
            sp.append('block up')
        if self.rect.bottom >= 550:
            sp.append('block down')
        return sp

    def update_moving(self):
        if self.mright and 'block right' not in self.possibility_of_movement():
            self.rect.centerx += 5
        if self.mleft and 'block left' not in self.possibility_of_movement():
            self.rect.centerx -= 5
        if self.mup and 'block up' not in self.possibility_of_movement():
            self.rect.centery -= 5
        if self.mdown and 'block down' not in self.possibility_of_movement():
            self.rect.centery += 5

    def update(self):
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
        else:
            self.timer1 = 0
            self.cur_frame = (self.cur_frame + 1) % len(self.afk)
            self.image = self.afk[self.cur_frame]





class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, spawn):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = load_image('bad_mario.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = spawn[0]
        self.rect.centery = spawn[1]

    def output(self):
        self.screen.blit(self.image, self.rect)

    def moving_away(self, player, hunting):
        if hunting:
            if self.rect.centerx < player.rect.centerx:
                self.rect.centerx += v
            else:
                self.rect.centerx -= v
            if self.rect.centery < player.rect.centery:
                self.rect.centery += v
            else:
                self.rect.centery -= v
        else:
            if 75 < self.rect.centerx < player.rect.centerx:
                self.rect.centerx -= v
            elif 730 > self.rect.centerx > player.rect.centerx:
                self.rect.centerx += v
            if 75 < self.rect.centery < player.rect.centery:
                self.rect.centery -= v
            elif 530 > self.rect.centery > player.rect.centery:
                self.rect.centery += v

    def shooting(self, player):
        if ((self.rect.centery - player.rect.centery) ** 2 + (
                self.rect.centerx - player.rect.centerx) ** 2) ** 0.5 > 125:
            new_bullet = bullets.Enemy_bullet(self.screen, self, player.rect.centerx, player.rect.centery)
            sprite_groups.enemys_bullets.add(new_bullet)
