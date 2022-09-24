#!/usr/bin/env python3

from board import Board
from snake import Snake, Direction
import sys
import pygame
import argparse

SNAKE_COLOR = 0, 150, 0
APPLE_COLOR = 200, 0, 0
BACKGROUND = 25, 25, 25

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', help='Width of the field', type=int, default=10)
    parser.add_argument('--tile_size', help='Pixel size of tiles', type=int, default = 64)
    parser.add_argument('--interval', help='Interval between game update (ms)', type=int, default=100)

    args = parser.parse_args()

    WIDTH = HEIGHT = args.size
    TILE_SIZE = args.tile_size
    BORDER_WIDTH = TILE_SIZE // 16
    INTERVAL = args.interval

    board = Board(WIDTH, HEIGHT)
    snake = Snake(board)

    pygame.init()
    size = width, height = WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE
    screen = pygame.display.set_mode(size)

    def draw_tile(x: int, y: int, color: pygame.Color):
        pygame.draw.rect(screen, color, pygame.Rect(
            x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        pygame.draw.rect(screen, BACKGROUND, pygame.Rect(
            x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), BORDER_WIDTH)

    board.gen_apple([])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        sys.exit()
                    case pygame.K_RIGHT:
                        snake.setDirection(Direction.RIGHT)
                    case pygame.K_LEFT:
                        snake.setDirection(Direction.LEFT)
                    case pygame.K_UP:
                        snake.setDirection(Direction.UP)
                    case pygame.K_DOWN:
                        snake.setDirection(Direction.DOWN)

        snake.take_action()
        snake.move()

        screen.fill(BACKGROUND)

        draw_tile(snake.x, snake.y, SNAKE_COLOR)

        for tailPiece in snake.tailPieces:
            draw_tile(tailPiece.x, tailPiece.y, SNAKE_COLOR)

        for apple in board.apples:
            pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(
                apple.x * TILE_SIZE, apple.y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0, TILE_SIZE // 2)

        pygame.display.flip()

        pygame.time.wait(INTERVAL)

        if not snake.alive:
            sys.exit()
