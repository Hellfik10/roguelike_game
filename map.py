from random import randint, sample
from load import load_image
import creatures
import sprite_groups


class Map:
    def __init__(self, width, height, screen):
        self.screen = screen

        self.rooms = []
        self.fon = None
        self.door_state = True

        self.coords = [[], []]

        for x in range(650):
            self.coords[0].append(x)

        for y in range(450):
            self.coords[1].append(y)

        self.width = width
        self.height = height

        self.fon_close_door = load_image('fon_close_door.jpeg')
        self.fon_open_door = load_image('fon_open_door.jpeg')

        self.new_level()

    def new_level(self):
        rooms_count = randint(4, 6)
        self.rooms = []
        self.fon = self.fon_open_door
        self.door_state = True

        for i in sprite_groups.player_group:
            i.player_pos((self.width // 2, self.height // 2))

        for i in range(rooms_count):
            if 'prize room' not in self.rooms:
                self.rooms.append('prize room')
            else:
                self.rooms.append('battle room')

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

            coords = self.coords.copy()

            x_or_y = ['x', 'y']

            block_coords = [[], []]

            for enemy_spawn in range(enemy_count):
                x_or_y_answer = sample(x_or_y, 1)[0]
                if x_or_y_answer == 'x':
                    coords[0] = list(set(coords[0]) - set(block_coords[0]))
                else:
                    coords[1] = list(set(coords[1]) - set(block_coords[1]))
                enemy_spawn_coords = [sample(coords[0], 1)[0], sample(coords[1], 1)[0]]
                enemy_spawn_coords = (enemy_spawn_coords[0] + 75, enemy_spawn_coords[1] + 75)
                new_enemy = creatures.Enemy(self.screen, enemy_spawn_coords, 1)
                sprite_groups.enemys.add(new_enemy)
                for x in range(enemy_spawn_coords[0] - 24, enemy_spawn_coords[0] + 24):
                    block_coords[0].append(x)
                for y in range(enemy_spawn_coords[1] - 40, enemy_spawn_coords[1] + 40):
                    block_coords[1].append(y)

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
