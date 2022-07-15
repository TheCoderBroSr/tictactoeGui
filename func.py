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

def boardCoordinates(pos):
    x, y = pos
    gap = pygame.display.get_surface().get_height()//3

    return (y//gap, x//gap) #Flipped due to pygame's coordinate system

def displayCoordinates(pos):
    x, y = pos
    gap = pygame.display.get_surface().get_height()//3

    return (y*gap, x*gap)

def is_board_full(board):
    full = 0

    for row in board:
        if all(marker != " " for marker in row):
            full += 1

    return full == len(board[0])

def win_check(board, markers):
    '''
    Returns winning marker as well as position of winning tiles
    '''
    winning_sequence = ([markers[0]]*3, [markers[1]]*3)

    for i in range(len(board)):
        #horizontal check
        if board[i] in winning_sequence:
            return board[i][0], (i + 0.5, 0), (i + 0.5, len(board[i])) #return first element in that row

        #vertical check
        col = [board[x][i] for x in range(len(board[i]))] #Get a column
        if col in winning_sequence:
            return col[0], (0, i+0.5), (len(board[i]), i+0.5) #return first element in that column

    #diagonal check
    diag1 = [board[x][x] for x in range(len(board))]
    diag2 = [board[y][abs(len(board) - y - 1)] for y in range(len(board))]

    if diag1 in winning_sequence:
        return diag1[0], (0, 0), (len(board), len(board))

    if diag2 in winning_sequence:
        return diag2[0], (0, len(board)), (len(board), 0)

    return -1, -1

def draw_bars(bars, color, surf):
    for bar in bars:
        pygame.draw.rect(surf, color, bar)

def draw_line(surf, color, pos, width):
    start_pos, end_pos = pos
    start_pos = (start_pos[0], start_pos[1])
    end_pos = (end_pos[0], end_pos[1])
    pygame.draw.line(surf, color, start_pos, end_pos, width)

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