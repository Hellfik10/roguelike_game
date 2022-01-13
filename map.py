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
        for i in sprite_groups.player_group:
            i.player_pos((self.width // 2, self.height // 2))

        rooms_count = randint(4, 6)

        self.rooms = []

        for i in range(rooms_count):
            if 'prize room' not in self.rooms:
                self.rooms.append('prize room')
            else:
                self.rooms.append('battle room')

        self.fon = self.fon_open_door
        self.door_state = True

        print(self.rooms)

    def generate_room(self):
        room = sample(self.rooms, 1)[0]

        del self.rooms[self.rooms.index(room)]

        if room == 'prize room':
            pass
        elif room == 'battle room':
            self.fon = self.fon_close_door
            self.door_state = False

            enemy_count = randint(4, 6)

            positions = sample(self.numbs, enemy_count)

            for i in range(enemy_count):
                new_enemy = creatures.Enemy(self.screen, self.possible_position[positions[i]])
                sprite_groups.enemys.add(new_enemy)

    def next_room(self, p):
        if p:
            if len(self.rooms) == 0:
                self.new_level()
            else:
                for i in sprite_groups.player_group:
                    i.player_pos((400, 525))

            self.generate_room()

    def pos_player_get(self):
        return self.pos_player

    def fon_get(self):
        fon_rect = self.fon.get_rect()

        return self.fon, fon_rect

    def door_state_get(self):
        if len(sprite_groups.enemys) == 0:
            self.fon = self.fon_open_door
            self.door_state = True

        return self.door_state
