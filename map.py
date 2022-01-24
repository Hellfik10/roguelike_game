from random import randint, sample
from load import load_image
import creatures
import environment
import sprite_groups
import items


class Map:
    def __init__(self, width, height, screen):

        self.screen = screen

        # загрузка видов бонусов и их расположения
        self.bonus = [items.HP, items.FastMovePlayer, items.FastMoveBulletsPlayer, items.MoreStrongerBulletsPlayer]
        self.bonus_coords = [[300, 300], [500, 300]]

        self.rooms = []

        self.fon = None
        self.door_state = True

        self.lvl = 0
        self.room = 0

        self.extra_hp = 0
        self.extra_speed_bullets = 0

        self.coords = [[], []]

        enemy = creatures.Enemy(self.screen, [0, 0], randint(1, 2), self.extra_hp, self.extra_speed_bullets)

        # загрузка координат в список вида [[координаты х], [координаты у]

        for x in range(0 + (enemy.rect.right - enemy.rect.left) // 2, 650 - (enemy.rect.right - enemy.rect.left) // 2):
            if x < 295 + (enemy.rect.right - enemy.rect.left) // 2 or \
                    x > 355 + (enemy.rect.right - enemy.rect.left) // 2:
                self.coords[0].append(x)

        for y in range(0 + (enemy.rect.bottom - enemy.rect.top) // 2, 450 - (enemy.rect.bottom - enemy.rect.top) // 2):
            if y < 380 - (enemy.rect.right - enemy.rect.left) // 2:
                self.coords[1].append(y)

        self.width = width
        self.height = height

        # загрузка заднего фона (дверь открыта, дверь закрыта)

        self.fon_close_door = load_image('fon_close_door.png')
        self.fon_open_door = load_image('fon_open_door.png')

        # генерация начальной комнаты

        self.new_level()

    def new_level(self):
        # количество комнат на уровне

        rooms_count = randint(4, 6)
        self.rooms = []

        # установка фона и состояния двери на открыто

        self.fon = self.fon_open_door
        self.door_state = True

        # подсчет уровней и сброс номера комнаты

        self.lvl += 1
        self.room = 0

        # установка позиции игрока

        for i in sprite_groups.player_group:
            i.player_pos((self.width // 2, self.height // 2))

        # добавление видов комнат в список self.rooms (обязательно присутствует призовая)

        for i in range(rooms_count):
            if 'prize room' not in self.rooms:
                self.rooms.append('prize room')
            else:
                self.rooms.append('battle room')

    def generate_room(self):
        # выбор комнаты которая будет генерироваться

        room = sample(self.rooms, 1)[0]
        del self.rooms[self.rooms.index(room)]

        # создание той или иной комнаты которую выбрал sample

        if room == 'prize room':

            # выбор вида бонусов

            bonus = sample(self.bonus, 2)

            # постановка на места

            for i in range(len(bonus)):
                sprite_groups.bonus_group.add(bonus[i](self.bonus_coords[i]))

        elif room == 'battle room':

            # закрытие двери и установка фона с закрытой дверью

            self.fon = self.fon_close_door
            self.door_state = False

            # кол-во противников

            enemy_count = randint(4, 6)

            # кол-во коробок

            box_count = randint(4, 6)

            coords = self.coords.copy()

            x_or_y = ['x', 'y']

            block_coords = [[], []]

            # выбор координат для коробок без их пересечения

            box_spawn_coords = [0, 0]

            enemy_for_coords = creatures.Enemy(self.screen, [0, 0], randint(1, 2),
                                            self.extra_hp, self.extra_speed_bullets)

            for box in range(box_count):
                x_or_y_answer = sample(x_or_y, 1)
                if x_or_y_answer == 'x':
                    if len(coords[0]) != 0:
                        box_spawn_coords = [sample(coords[0], 1)[0], sample(self.coords[1], 1)[0]]
                    else:
                        box_spawn_coords = [sample(self.coords[0], 1)[0], sample(coords[1], 1)[0]]
                else:
                    if len(coords[1]) != 0:
                        box_spawn_coords = [sample(self.coords[0], 1)[0], sample(coords[1], 1)[0]]
                    else:
                        box_spawn_coords = [sample(coords[0], 1)[0], sample(self.coords[1], 1)[0]]
                box = environment.Box(box_spawn_coords)
                sprite_groups.environment_group.add(box)
                for x in range(box_spawn_coords[0] - (enemy_for_coords.rect.right - enemy_for_coords.rect.left),
                               box_spawn_coords[0] + (enemy_for_coords.rect.right - enemy_for_coords.rect.left)):
                    block_coords[0].append(x)
                for y in range(box_spawn_coords[1] - (box.rect.bottom - box.rect.top),
                               box_spawn_coords[1] + (box.rect.bottom - box.rect.top)):
                    block_coords[1].append(y)
                coords[0] = list(set(coords[0]) - set(block_coords[0]))
                coords[1] = list(set(coords[1]) - set(block_coords[1]))


                # выбор координат для врагов без пересечения с коробками


            for enemy_spawn in range(enemy_count):
                x_or_y_answer = sample(x_or_y, 1)
                if x_or_y_answer == 'x':
                    if len(coords[0]) != 0:
                        enemy_spawn_coords = [sample(coords[0], 1)[0], sample(self.coords[1], 1)[0]]
                    else:
                        enemy_spawn_coords = [sample(self.coords[0], 1)[0], sample(coords[1], 1)[0]]
                else:
                    if len(coords[1]) != 0:
                        enemy_spawn_coords = [sample(self.coords[0], 1)[0], sample(coords[1], 1)[0]]
                    else:
                        enemy_spawn_coords = [sample(coords[0], 1)[0], sample(self.coords[1], 1)[0]]
                new_enemy = creatures.Enemy(self.screen, enemy_spawn_coords, randint(1, 2),
                                            self.extra_hp, self.extra_speed_bullets)
                sprite_groups.enemys.add(new_enemy)
                for x in range(box_spawn_coords[0] - 20,
                               box_spawn_coords[0] + 20):
                    block_coords[0].append(x)
                for y in range(box_spawn_coords[1] - 20,
                               box_spawn_coords[1] + 20):
                    block_coords[1].append(y)
                coords[0] = list(set(coords[0]) - set(block_coords[0]))
                coords[1] = list(set(coords[1]) - set(block_coords[1]))

    def next_room(self, p):

        # проверака на возможность перемещения в следующую локацию

        if p:

            # удаление спрайтов коробок и бонусов

            sprite_groups.environment_group.empty()
            sprite_groups.bonus_group.empty()

            # если кол-во комнат = 0 новый уровень и усложнение врагов, если нет, то переход в следующую комнату

            if len(self.rooms) == 0:
                self.new_level()
                self.extra_hp += 1
                if self.extra_speed_bullets != 10:
                    self.extra_speed_bullets += 1
            else:
                for i in sprite_groups.player_group:
                    i.player_pos((400, 525))
                self.room += 1

            self.generate_room()

    def pos_player_get(self):

        # возвращение нужной позиции игрока

        return self.pos_player

    def fon_get(self):
        fon_rect = self.fon.get_rect()

        # передача фона для отрисовки

        return self.fon, fon_rect

    def door_state_get(self):

        # если врагов нет то открыть дверь и заменить на фон с открытой дверью и вернуть состояние двери

        if len(sprite_groups.enemys) == 0:
            self.fon = self.fon_open_door
            self.door_state = True

        return self.door_state
