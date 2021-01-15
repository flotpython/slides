import pygame

from itertools import product

# la taille du jeu en nombre de cellules
BOARD_SIZE = (20, 20)
BOARD_WIDTH, BOARD_HEIGHT = BOARD_SIZE

# la taille d'une cellule en nombre de pixels
CELL_SIZE = (15, 15)
CELL_WIDTH, CELL_HEIGHT = CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Screen:

    pygame_inited = False

    def __init__(self):

        if not Screen.pygame_inited:
            pygame.init()
            # pygame.display.set_caption("multi-player")
            Screen.pygame_inited = True

        self.screen = pygame.display.set_mode(
            (BOARD_WIDTH*CELL_WIDTH, BOARD_HEIGHT*CELL_HEIGHT))

    def size(self):
        return BOARD_WIDTH, BOARD_HEIGHT

    def draw_cell(self, board_x, board_y, color=WHITE):
        screen_x, screen_y = CELL_WIDTH * board_x, CELL_HEIGHT * board_y
        for x, y in product(range(CELL_WIDTH), range(CELL_HEIGHT)):
            screen_coords = screen_x + x, screen_y + y
            self.screen.set_at(screen_coords, color)

    def display(self, players):
        """
        players is an iterable of dictionaries
        b'color' -> [r g b], b'position' -> [x, y]
        """
        self.screen.fill(BLACK)
        for player in players:
            x, y = player[b'position']
            color = player[b'color']
            self.draw_cell(x, y, color)
        pygame.display.update()
