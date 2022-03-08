from random import randint
import sys
import pygame
from pygame.sprite import Sprite
import time as t

class Settings():

    def __init__(self) -> None:
        self.to_live = [1,3,5,8]
        self.to_ressurect = [3,5,7]
        self.screen_width = 500
        self.screen_height = 500

        self.cell_size = 5
        self.number_of_rows = int(self.screen_width / self.cell_size)
        self.number_of_cols = int(self.screen_height / self.cell_size)

class Cell(Sprite):

    heigth, width = 5, 5     

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([Cell.width, Cell.heigth])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()


class GameOfLife:

    def __init__(self) -> None:
        pygame.init()
        
        self.settings = Settings()
        self.cells = list()
        self.next_generation = []
        for i in range(self.settings.number_of_rows):
            self.next_generation.append([0] * self.settings.number_of_cols)


        for i in range(self.settings.number_of_rows):
            self.cells.append([0] * self.settings.number_of_cols)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Game Of Life")


    def _randomize_life(self):

        for i in range(self.settings.number_of_rows):
            self.cells[i] = ([0] * self.settings.number_of_cols)

        for i in range(500):
            y = randint(0,99)
            x = randint(0,99)
            self.cells[y][x] = 1


    def _count_neighbours(self, y, x):
        neighbours = 0

        if y == 0:
            return

        if x == 0:
            return

        if x >= self.settings.number_of_cols - 1:
            return

        if y >= self.settings.number_of_rows - 1:
            return

        if self.cells[y-1][x-1]:
            neighbours += 1
        if self.cells[y-1][x]:
            neighbours += 1
        if self.cells[y-1][x+1]:
            neighbours += 1

        if self.cells[y][x-1]:
            neighbours += 1
        if self.cells[y][x+1]:
            neighbours += 1

            
        if self.cells[y+1][x-1]:
            neighbours += 1
        if self.cells[y+1][x]:
            neighbours += 1
        if self.cells[y+1][x+1]:
            neighbours += 1

        return neighbours

    def _calculate_next_gen(self):

        for y in range(self.settings.number_of_rows):
            for x in range(self.settings.number_of_cols):
                neighbours = self._count_neighbours(y,x)
                
                if (neighbours in self.settings.to_live) and self.cells[y][x]:
                    self.next_generation[y][x] = 1
                    
                elif neighbours in self.settings.to_ressurect:
                    self.next_generation[y][x] = 1
                
                else:
                    self.next_generation[y][x] = 0


        self.cells = self.next_generation

    def run_game(self):
        """Start main game"""
        self.start = t.time()
        self._randomize_life()
        while True:
            # a = input("w")
            pygame.time.Clock().tick(25)
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


    def _draw_life(self):

        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                if self.cells[row][col]:
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(row*5,col*5,5,5))
                else:
                    pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(row*5,col*5,5,5))

    def _update_screen(self):
        """Update objects on screen"""
        self._draw_life()
        pygame.display.flip()

    def _generate_cells(self):

        for row_number in range(len(self.life)):
            for column_number in range(len(self.life[row_number])):
                tile = Cell()
                tile.rect.x = column_number * 5
                tile.rect.y = row_number * 5
                self.tiles.add(tile)



if __name__ == "__main__":
    gof = GameOfLife()
    gof.run_game()