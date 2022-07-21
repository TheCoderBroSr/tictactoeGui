import sys
import pygame

pygame.font.init()

def end():
    '''
    ends game
    '''

    pygame.quit()
    sys.exit()

def init_board():
    '''
    Returns an empty n by n matrix/board
    '''

    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def boardCoordinates(pos:tuple) -> tuple:
    '''
    Converts Mouse/Display Coordinates to Board Coordinates
    '''

    x, y = pos
    gap = pygame.display.get_surface().get_height()//3

    return (y//gap, x//gap) #Flipped due to pygame's coordinate system

def displayCoordinates(pos:tuple) -> tuple:
    '''
    Converts Board Coordinates to Display Coordinates
    '''

    x, y = pos
    gap = pygame.display.get_surface().get_height()//3

    return (y*gap, x*gap)

def is_board_full(board : list[list]) -> bool:
    '''
    Checks if each row in the board is full
    '''

    no_full_rows = sum(1 for row in board if all(marker != " " for marker in row))
    return no_full_rows == len(board[0])

def win_check(board:list[list], markers:list):
    '''
    Returns winning marker as well as position of winning tiles
    '''
    winning_sequence = ([markers[0]]*3, [markers[1]]*3)
    offset = 0.5

    #Adding offset to board pos. as offset for when we add the game win lines
    for i in range(len(board)):
        #horizontal check
        if board[i] in winning_sequence:
            return board[i][0], (i + offset, 0), (i + offset, len(board[i])) #return first element in that row

        #vertical check
        col = [board[x][i] for x in range(len(board[i]))] #Get a column
        if col in winning_sequence:
            return col[0], (0, i+offset), (len(board[i]), i+offset) #return first element in that column

    #diagonal check
    diag1 = [board[x][x] for x in range(len(board))]
    diag2 = [board[y][abs(len(board) - y - 1)] for y in range(len(board))]

    if diag1 in winning_sequence:
        return diag1[0], (0, 0), (len(board), len(board))

    if diag2 in winning_sequence:
        return diag2[0], (0, len(board)), (len(board), 0)

    return -1, -1

def draw_bars(bars:list, color:str, surf:pygame.Surface):
    for bar in bars:
        pygame.draw.rect(surf, color, bar)

def draw_line(surf:pygame.Surface, color:str, pos:tuple, width:int):
    start_pos, end_pos = pos
    start_pos = (start_pos[0], start_pos[1])
    end_pos = (end_pos[0], end_pos[1])
    pygame.draw.line(surf, color, start_pos, end_pos, width)

def display_board(board:list[list], color:str, MARKERS:list, surf:pygame.Surface):
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
            marker_index = 0

            if val==" ":
                continue
            
            if val == "O":
                marker_index = 1
            
            val = MARKERS[marker_index]
            surf.blit(val, (gap*j - (val.get_width()//2) + (gap//2), gap*i - (val.get_height()//2) + (gap//2)))