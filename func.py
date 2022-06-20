import sys
import pygame

pygame.font.init()
PAWN = pygame.font.SysFont('Arial', 150)

def end():
    pygame.quit()
    sys.exit()

def init_board():
    return [["N"]*3]*3

def draw_bars(bars, color, surf):
    for bar in bars:
        pygame.draw.rect(surf, color, bar)

def display_board_bars(horizontal_bars, vertical_bars, color, surf):
    draw_bars(horizontal_bars, color, surf)
    draw_bars(vertical_bars, color, surf)

def display_board(board, color, surf):
    row_gap = 200
    val_gap = 200

    for i in range(len(board[0])):
        for j in range(len(board[i])):
            val = board[i][j]

            if val=="N":
                continue

            val = PAWN.render(val, 1, color)
            surf.blit(val, (val_gap*j - (val.get_width()//2) + (val_gap//2), row_gap*i - (val.get_height()//2) + (row_gap//2)))