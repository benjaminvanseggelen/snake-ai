from board import Board
from snake import Snake
import sys
import pygame
import time

WIDTH = 20
HEIGHT = 20
TILE_SIZE = 64
BORDER_WIDTH = 4

SNAKE_COLOR = 0, 150, 0
BACKGROUND = 25, 25, 25

INTERVAL = 1

if __name__ == "__main__":
    board = Board(8, 8)
    snake = Snake(board)

    pygame.init()
    size = width, height = WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE
    screen = pygame.display.set_mode(size)

    def draw_tile(x: int, y: int, color: pygame.Color):
        pygame.draw.rect(screen, color, pygame.Rect(
            x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        pygame.draw.rect(screen, BACKGROUND, pygame.Rect(
            x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), BORDER_WIDTH)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(BACKGROUND)

        draw_tile(snake.x, snake.y, SNAKE_COLOR)

        for tailPiece in snake.tailPieces:
            draw_tile(tailPiece.x, tailPiece.y, SNAKE_COLOR)

        pygame.display.flip()
        time.sleep(INTERVAL)
