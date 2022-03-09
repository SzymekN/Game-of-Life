from random import randint
import sys
from unittest import result
import pygame
from pygame.sprite import Sprite
import time as t
import copy

class Settings():

    def __init__(self) -> None:
        self.to_live = [1,2,5]
        self.to_ressurect = [3,6]
        self.screen_width = 1000
        self.screen_height = 1000

        self.cell_size = 4
        self.number_of_rows = int(self.screen_height / self.cell_size)
        self.number_of_cols = int(self.screen_width / self.cell_size)

class Cell(Sprite):

    heigth, width = 1,1    

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([Cell.width, Cell.heigth])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()



def timer(func):

    def wrapper(*args, **kwargs):
        start = t.time()
        result = func(*args, **kwargs)
        end = t.time()
        print(f"Function {func.__name__!r} executed in {(end-start)}s")
        return result
    return wrapper

class GameOfLife:

    def __init__(self) -> None:
        pygame.init()
        
        self.settings = Settings()
        self.cells = []
        self.next_generation = []
        for i in range(self.settings.number_of_rows):
            self.next_generation.append([0] * self.settings.number_of_cols)


        for i in range(self.settings.number_of_rows):
            self.cells.append([0] * self.settings.number_of_cols)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Game Of Life")

    @timer
    def _randomize_life(self):

        for i in range(self.settings.number_of_rows):
            self.cells[i] = ([0] * self.settings.number_of_cols)

        # for i in range(int(self.settings.number_of_cols * self.settings.number_of_rows / 20)):
        for i in range(int(5000)):
            y = randint(0,self.settings.number_of_rows-1)
            x = randint(0,self.settings.number_of_cols-1)
            self.cells[y][x] = 1

    def _count_neighbours(self, y, x):
        neighbours = 0

        xl = xr = x
        yb = yt = y

        if y == 0:
            yb = self.settings.number_of_rows
        elif y >= self.settings.number_of_rows - 1:
            yt = -1

        if x == 0:
            xl = self.settings.number_of_cols
        elif x >= self.settings.number_of_cols-1:
            xr = -1

        if self.cells[yb-1][x]:
            neighbours += 1

        if self.cells[yb-1][xl-1]:
            neighbours += 1

        if self.cells[yb-1][xr+1]:
            neighbours += 1

        if self.cells[y][xl-1]:
            neighbours += 1
        if self.cells[y][xr+1]:
            neighbours += 1

            
        if self.cells[yt+1][xl-1]:
            neighbours += 1
        if self.cells[yt+1][x]:
            neighbours += 1
        if self.cells[yt+1][xr+1]:
            neighbours += 1
        


        return neighbours

    @timer
    def _calculate_next_gen(self):


        for y in range(self.settings.number_of_rows):
            for x in range(self.settings.number_of_cols):
                neighbours = self._count_neighbours(y,x)
                
                if neighbours in self.settings.to_live and self.cells[y][x]:
                    self.next_generation[y][x] = 1
                    
                elif neighbours in self.settings.to_ressurect and not self.cells[y][x]:
                    self.next_generation[y][x] = 1
                
                else:
                    self.next_generation[y][x] = 0


        self.cells = copy.deepcopy(self.next_generation)

    def run_game(self):
        """Start main game"""
        self.start = t.time()
        self._randomize_life()
        while True:
            # a = input("w")
            pygame.time.Clock().tick(30)
            self._check_events()
            self._update_screen()
            self._calculate_next_gen()

    def _check_events(self):
            """Respond if event occurs"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check keydown event triggered"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Check keydown event triggered"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    @timer
    def _draw_life(self):

        s = self.settings.cell_size

        for row in range(self.settings.number_of_rows):
            for col in range(self.settings.number_of_cols):
                if self.cells[row][col]:
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(col*s,row*s,s,s))
                else:
                    pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(col*s,row*s,s,s))

    def _update_screen(self):
        """Update objects on screen"""
        self._draw_life()
        pygame.display.flip()




if __name__ == "__main__":
    gof = GameOfLife()
    gof.run_game()