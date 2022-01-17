import pygame
import sprite_groups
pygame.font.init()


class Interface:
    def __init__(self):
        self.HP = 0
        self.lvl = 0
        self.room = 0
        self.font = pygame.font.Font('fonts/pixar-one.otf', 36)

    def output(self, hp, lvl, room):
        text_hp = self.font.render(f'X{hp}', True, 'black')
        text_lvl_room = self.font.render(f'{lvl}-{room}', True, 'black')
        text_lvl_room_rect = text_lvl_room.get_rect()
        return [text_hp, text_lvl_room, 790 - text_lvl_room_rect.right - text_lvl_room_rect.left]
