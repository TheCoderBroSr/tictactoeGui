import pygame
import func

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(("TicTacToe GUI"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()
        
