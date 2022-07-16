import pygame
from func import *

pygame.init()
board = init_board()

GAME_LOOP = True
SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(("TicTacToe GUI"))
FPS = 30
clock = pygame.time.Clock()

MARKER_SIZE = SCREEN_WIDTH//4
MARKER_FONT = pygame.font.SysFont('Arial', MARKER_SIZE)

BLACK = (10, 4, 20)
GREY = (35, 10, 55)
BLUE = (75, 23, 103)
RED = (103, 23, 55)

MARKER = "X"
GAME_END = -1 #-1 -> Game not end, 1 -> Game has been won/tie, 2 -> Init Game End Sequence

while GAME_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            i, j = boardCoordinates(mouse_pos)

            if board[i][j] == " ":
                board[i][j] = MARKER

                if MARKER == "X":
                    MARKER = "O"
                else:
                    MARKER = "X"

            w_marker, *w_pos = win_check(board, ["X", "O"])

            if w_marker == -1:
                if is_board_full(board):
                    print("Tie")
                    GAME_END = 2
            else:
                w_pos = list(map(displayCoordinates, w_pos))
                GAME_END = 1
                print(f"{w_marker} WON!!!")

    WIN.fill(BLACK)
    display_board(board, [(RED, BLUE), GREY], MARKER_FONT, WIN)

    if GAME_END == 1:
        draw_line(WIN, [RED, BLUE][MARKER=="X"], w_pos, 15)
        GAME_END = 2

    pygame.display.update()
    clock.tick(FPS)
        
    if GAME_END == 2:
        pygame.time.delay(2000)
        GAME_LOOP = False