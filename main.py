import pygame
from func import *

pygame.init()
board = init_board()

GAME_LOOP = True
SCREEN_WIDTH = 500
SCREEN_HEIGHT = SCREEN_WIDTH
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(("TicTacToe GUI"))
FPS = 30
clock = pygame.time.Clock()

MARKER_SIZE = SCREEN_WIDTH//4
MARKER_FONT = pygame.font.SysFont('Arial', MARKER_SIZE)
MARKER_X = pygame.image.load("assets/X.png")
MARKER_O = pygame.image.load("assets/O.png")
WIN_STRIKE_LENGTH = SCREEN_WIDTH//25

BLACK = (10, 4, 20)
GREY = (35, 10, 55)
BLUE = (103, 23, 75)
RED = (103, 23, 55)

MARKER_SIZE = SCREEN_WIDTH//5
MARKER_POINTS = (MARKER_SIZE, MARKER_SIZE)
MARKER_X = pygame.transform.scale(MARKER_X, MARKER_POINTS)
MARKER_O = pygame.transform.scale(MARKER_O, MARKER_POINTS)
MARKERS = [MARKER_X, MARKER_O]
MARKER = "X"
GAME_END = -1 #-1 -> Game not end, 1 -> Game has been won, 2 -> Init Game End Sequence

while GAME_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Ensures that marker is placed only on left mouseclick
            mouse_pos = event.pos
            i, j = boardCoordinates(mouse_pos)

            if board[i][j] == " ": #Check if board at that pos. is empty
                board[i][j] = MARKER #Add marker

                #Change Current Marker i.e. Change the player
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

    WIN.fill(BLACK)
    display_board(board, [(RED, BLUE), GREY], MARKERS, WIN)

    #If Game has been won
    if GAME_END == 1:
        draw_line(WIN, [RED, BLUE][MARKER=="O"], w_pos, WIN_STRIKE_LENGTH)
        print(f"{w_marker} WON!!!")
        GAME_END = 2

    pygame.display.update()
    clock.tick(FPS)
        
    #Game end sequence
    if GAME_END == 2:
        pygame.time.delay(1500)
        GAME_LOOP = False