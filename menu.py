import pygame

font = pygame.font.Font('fonts/pixar-one.otf', 36)

class Menu:
    def __init__(self):
        self.option_surfaces = []
        self.callbacks = []
        self.current_option_index = 0

    def append_option(self, option, callback):
        self.option_surfaces.append(font.render(option, True, 'White'))
        self.callbacks.append(callback)

    def switch(self, dir):
        self.current_option_index = max(0, min(self.current_option_index + dir, len(self.option_surfaces) - 1))

    def select(self):
        return self.callbacks[self.current_option_index]

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self.option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self.current_option_index:
                pygame.draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)