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

GAME_FONT = "assets/game_font.otf"
GAME_SCORE = [0,0] #X wins, O wins
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
                    GAME_END = 0.5 #Tie
            else:
                w_pos = list(map(displayCoordinates, w_pos))

                if w_marker == "X":
                    GAME_SCORE[0] += 1
                else:
                    GAME_SCORE[1] += 1

                GAME_END = 1

    WIN.fill(BLACK)
    display_board(board, [(RED, BLUE), GREY], MARKERS, WIN)

    text(WIN, GAME_FONT, (SCREEN_WIDTH//2, 30), f"{GAME_SCORE[0]} - {GAME_SCORE[1]}", 50, (255, 255, 255))

    #Done this way to show msg
    if GAME_END == 1.75:
        pygame.time.delay(1000)
        text(WIN, GAME_FONT, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), "TIE", round(SCREEN_WIDTH/2.65), (120, 205, 165))
        GAME_END = 2

    if GAME_END == 1.5:
        pygame.time.delay(1000)
        draw_line(WIN, [RED, BLUE][MARKER=="O"], w_pos, WIN_STRIKE_LENGTH)
        text(WIN, GAME_FONT, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), f"{w_marker} WON", round(SCREEN_WIDTH/2.65), (100, 30, 165))
        GAME_END = 2
    
    if GAME_END == 0.5:
        GAME_END = 1.75

    #If Game has been won
    if GAME_END == 1:
        draw_line(WIN, [RED, BLUE][MARKER=="O"], w_pos, WIN_STRIKE_LENGTH)
        GAME_END = 1.5
    

    pygame.display.update()
    clock.tick(FPS)
        
    #Game end sequence
    if GAME_END == 2:
        pygame.time.delay(1750)
        GAME_END = False
        board = init_board()
        MARKER = "X"