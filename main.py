from random import randint
from turtle import width
import pygame
from pygame.sprite import Sprite
import time as t

class Settings():

    def __init__(self) -> None:
        self.to_live = [2,3]
        self.to_ressurect = [3]
        self.screen_width = 500
        self.screen_height = 500

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
        self.cells = pygame.sprite.Group()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Game Of Life")

        self.cells = pygame.sprite.Group()

    def run_game(self):
        """Start main game"""
        self.start = t.time()
        while True:
            # a = input("w")
            pygame.time.Clock().tick(30)
            self._update_screen()

    def _update_screen(self):
        """Update objects on screen"""
        self.cells.draw(self.screen)

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