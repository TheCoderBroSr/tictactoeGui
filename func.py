import sys
import pygame

pygame.font.init()

def end():
    pygame.quit()
    sys.exit()

def init_board():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def gridCoordinates(pos, surf):
    x, y = pos
    gap = surf.get_height()//3

    return (y//gap, x//gap) #Flipped due to pygame's coordinate system

def is_board_full(board):
    full = 0

    for row in board:
        if all(marker != " " for marker in row):
            full += 1

    return full == len(board[0])

def win_check(board, markers):
    for i in range(len(board)):
        #Horizontal check
        if board[i] in ([markers[0]]*3, [markers[1]]*3):
            return board[i][0]

        #Vertical check
        elif [board[z][i] for z in range(len(board[i]))] in ([markers[0]]*3, [markers[1]]*3):
            return board[i][0]

        #Diagonal check
        elif ([board[z][z] for z in range(len(board[i]))] in ([markers[0]]*3, [markers[1]]*3)):
            return board[i][i]
        
        elif ([board[z][len(board[i])-z-1] for z in range(len(board[i]))] in ([markers[0]]*3, [markers[1]]*3)):
            return board[i][len(board) - i - 1]

        else:
            return -1
    return -1

def draw_bars(bars, color, surf):
    for bar in bars:
        pygame.draw.rect(surf, color, bar)

def display_board(board, color, MARKER, surf):
    #color is a list, where in first index is the colors of the markers,
    #and in second is the color of the bars
    height, width = surf.get_height(), surf.get_width() #Getting height and width of surface

    gap = height/3 #Getting the gap in the grid
    bar_thickness = int((1/60) * height)

    horizontal_bars = [pygame.Rect(int(i*gap), 0, bar_thickness, height) for i in range(1, 3)] #Getting horizontal bars of the grid
    vertical_bars = [pygame.Rect(0, int(i*gap), width, bar_thickness) for i in range(1, 3)] #Getting vertical bars of the grid

    #Drawing individual bar of each type
    draw_bars(horizontal_bars, color[1], surf)
    draw_bars(vertical_bars, color[1], surf)

    #Drawing value of each grid cell
    for i in range(len(board[0])):
        for j in range(len(board[i])):
            val = board[i][j]
            color_index = 0

            if val==" ":
                continue
            
            if val == "O":
                color_index = 1
            
            val = MARKER.render(val, 1, color[0][color_index])
            surf.blit(val, (gap*j - (val.get_width()//2) + (gap//2), gap*i - (val.get_height()//2) + (gap//2)))