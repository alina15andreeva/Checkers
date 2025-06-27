import pygame
import time
from checkers_game.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK
from checkers_game.game import Game
from minimax.algorithm_alphabeta import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == BLACK:
            start_time = time.time()
            value, new_board, nodes_per_depth = minimax(game.get_board(), 5, BLACK, game, float('-inf'), float('inf'))
            game.ai_move(new_board)
            end_time = time.time()
            print("Time taken for Black's move:", end_time - start_time, "seconds")
            print("Nodes per depth:", nodes_per_depth)

        if game.winner() is not None:
            print(game.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        
        game.update()

    pygame.quit()

main()
