from random import randint, sample
from load import load_image
import creatures
import environment
import sprite_groups
import items


class Map:
    def __init__(self, width, height, screen):
        self.screen = screen

        self.bonus = [items.HP, items.FastMovePlayer, items.FastMoveBulletsPlayer]
        self.bonus_coords = [[300, 300], [500, 300]]

        self.rooms = []
        self.fon = None
        self.door_state = True

        self.coords = [[], []]

        enemy = creatures.Enemy(self.screen, [0, 0], randint(1, 2))

        for x in range(0 + (enemy.rect.right - enemy.rect.left) // 2, 650 - (enemy.rect.right - enemy.rect.left) // 2):
            self.coords[0].append(x)

        for y in range(0 + (enemy.rect.bottom - enemy.rect.top) // 2, 450 - (enemy.rect.bottom - enemy.rect.top) // 2):
            self.coords[1].append(y)

        self.width = width
        self.height = height

        self.fon_close_door = load_image('fon_close_door.png')
        self.fon_open_door = load_image('fon_open_door.png')

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

    def generate_room(self):
        room = sample(self.rooms, 1)[0]
        del self.rooms[self.rooms.index(room)]
        if room == 'prize room':
            bonus = sample(self.bonus, 2)
            for i in range(len(bonus)):
                sprite_groups.bonus_group.add(bonus[i](self.bonus_coords[i]))
        elif room == 'battle room':
            self.fon = self.fon_close_door
            self.door_state = False

            enemy_count = randint(4, 6)

            box_count = randint(1, 3)

            coords = self.coords.copy()

            x_or_y = ['x', 'y']

            block_coords = [[], []]

            for box in range(box_count):
                x_or_y_answer = sample(x_or_y, 1)[0]
                if x_or_y_answer == 'x':
                    coords[0] = list(set(coords[0]) - set(block_coords[0]))
                else:
                    coords[1] = list(set(coords[1]) - set(block_coords[1]))
                box_spawn_coords = [sample(coords[0], 1)[0], sample(coords[1], 1)[0]]
                box = environment.Box(box_spawn_coords)
                sprite_groups.environment_group.add(box)
                for x in range(box_spawn_coords[0] - (box.rect.right - box.rect.left) // 2,
                               box_spawn_coords[0] + (box.rect.right - box.rect.left) // 2):
                    block_coords[0].append(x)
                for y in range(box_spawn_coords[1] - (box.rect.bottom - box.rect.top) // 2,
                               box_spawn_coords[1] + (box.rect.bottom - box.rect.top) // 2):
                    block_coords[1].append(y)

            for enemy_spawn in range(enemy_count):
                x_or_y_answer = sample(x_or_y, 1)[0]
                if x_or_y_answer == 'x':
                    coords[0] = list(set(coords[0]) - set(block_coords[0]))
                else:
                    coords[1] = list(set(coords[1]) - set(block_coords[1]))
                enemy_spawn_coords = [sample(coords[0], 1)[0], sample(coords[1], 1)[0]]
                new_enemy = creatures.Enemy(self.screen, enemy_spawn_coords, randint(1, 2))
                sprite_groups.enemys.add(new_enemy)
                for x in range(enemy_spawn_coords[0] - (new_enemy.rect.right - new_enemy.rect.left) // 2,
                               enemy_spawn_coords[0] + (new_enemy.rect.right - new_enemy.rect.left) // 2):
                    block_coords[0].append(x)
                for y in range(enemy_spawn_coords[1] - (new_enemy.rect.bottom - new_enemy.rect.top) // 2,
                               enemy_spawn_coords[1] + (new_enemy.rect.bottom - new_enemy.rect.top) // 2):
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
