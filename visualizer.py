from sorters import *
import pygame
import sys
import random

class Visualizer:
    methods = {
        "bubble": BubbleSorter,
        "elijah": ElijahSorter
    }

    def __init__(self,
                 data='auto',
                 win_width=700,
                 win_height=500,
                 space=0.5,
                 line_width=5,
                 fill_color=(255,255,255),
                 background_color=(0,0,0)
                 ):
        if data == 'auto':
            data = [random.randint(10000, 100000) for _ in range(int(win_width/(space+line_width)))]

        self.data = data
        self.is_init = False
        self.win_width = win_width
        self.win_height = win_height
        self.space = space
        self.line_width = line_width
        self.fill_color = fill_color
        self.background_color = background_color
        self.max_line_height = 70*self.win_height/100
        self.screen = None

    @staticmethod
    def normalize(mylist, upper=1):
        min_nb = min(mylist)
        max_nb = max(mylist)
        new = [
            (upper * (x - min_nb)) / (max_nb - min_nb)
            for x in mylist
        ]
        return new

    def render(self, sorting_method):
        if not self.is_init:
            self._init_render()

        sorter_cls = Visualizer.methods[sorting_method.lower()]
        sorter_iter = iter(sorter_cls(self.data))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            try:
                sorter_state, current_indexes = next(sorter_iter)
            except StopIteration:
                continue

            normalized_state = self.normalize(sorter_state, self.max_line_height)

            for ix, num in enumerate(normalized_state):
                color = self.fill_color
                if ix in current_indexes:
                    color = (255,0,0)
                y = self.win_height - (num)
                x = ix * (self.line_width + self.space)
                pygame.draw.line(self.screen, color, (x,y), (x, self.win_height), self.line_width)
                pygame.draw.line(self.screen, self.background_color, (x,0), (x,y), self.line_width)
            pygame.display.update()

    def _init_render(self):
        self.is_init = True
        pygame.init()
        self.screen = pygame.display.set_mode((self.win_width, self.win_height))
        self.screen.fill(self.background_color)
        pygame.display.update()
