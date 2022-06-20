import pygame
from func import *

pygame.init()
board = [["X", "O", "N"], 
        ["X", "O", "N"], 
        ["N", "X", "O"]]

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(("TicTacToe GUI"))

BLACK = (5, 0, 20)
BLUE = (10, 23, 123)

gap = SCREEN_HEIGHT//3
horizontal_bars = [pygame.Rect(i*gap, 0, 10, SCREEN_HEIGHT) for i in range(1, 3)]
vertical_bars = [pygame.Rect(0, i*gap, SCREEN_WIDTH, 10) for i in range(1, 3)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end()

    WIN.fill(BLACK)

    display_board_bars(horizontal_bars, vertical_bars, BLUE, WIN)
    display_board(board, BLUE, WIN)

    pygame.display.update()
        
