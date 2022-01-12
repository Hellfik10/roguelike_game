from random import randint, sample
from load import load_image
import creatures
import sprite_groups


class Map:
    def __init__(self, width, height, screen):
        self.screen = screen

        self.width = width
        self.height = height

        self.fon_close_door = load_image('fon_close_door.jpeg')
        self.fon_open_door = load_image('fon_open_door.jpeg')

        self.new_level()

        self.possible_position = {1: (90, 510), 2: (90, 90), 3: (710, 90), 4: (710, 510), 5: (90, 300), 6: (710, 300),
                                  7: (180, 180), 8: (180, 420), 9: (620, 180), 10: (620, 420), 11: (300, 300),
                                  12: (500, 300), 13: (300, 180), 14: (500, 180), 15: (400, 250), 16: (400, 350)}
        self.numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def new_level(self):
        self.pos_player = (self.width // 2, self.height // 2)
        self.rooms_count = randint(4, 6)
        self.fon = self.fon_open_door
        self.door_state = True

    def generate_room(self):
        self.fon = self.fon_close_door
        self.pos_player = (self.width // 2, 530)
        self.door_state = False
        enemy_count = randint(4, 6)
        positions = sample(self.numbs, enemy_count)

        for i in range(enemy_count):
            new_enemy = creatures.Enemy(self.screen, self.possible_position[positions[i]])
            sprite_groups.enemys.add(new_enemy)

    def next_room(self, p):
        if p:
            self.generate_room()

    def pos_player_get(self):
        return self.pos_player

    def fon_get(self):
        fon_rect = self.fon.get_rect()
        return self.fon, fon_rect

    def door_state_get(self):
        return self.door_state
