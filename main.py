import pygame
from func import *

pygame.init()
board = init_board()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(("TicTacToe GUI"))
FPS = 30
clock = pygame.time.Clock()

MARKER_SIZE = SCREEN_WIDTH//4
MARKER_FONT = pygame.font.SysFont('Comic Sans Ms', MARKER_SIZE)

BLACK = (10, 4, 20)
BLUE = (10, 23, 123)
RED = (43, 23, 100)

MARKER = "X"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            i, j = gridCoordinates(mouse_pos, WIN)

            if board[i][j] == " ":
                board[i][j] = MARKER

                if MARKER == "X":
                    MARKER = "O"
                else:
                    MARKER = "X"

    WIN.fill(BLACK)
    display_board(board, [(RED, BLUE), BLUE], MARKER_FONT, WIN)

    print(win_check(board, ["X", "O"]), board)

    pygame.display.update()
    clock.tick(FPS)
        
