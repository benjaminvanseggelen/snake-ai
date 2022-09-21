from board import Board
from snake import Snake, Direction
import sys
import pygame

WIDTH = 20
HEIGHT = 20
TILE_SIZE = 64
BORDER_WIDTH = 4

SNAKE_COLOR = 0, 150, 0
APPLE_COLOR = 200, 0, 0
BACKGROUND = 25, 25, 25

INTERVAL = 300

if __name__ == "__main__":
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
                    case pygame.QUIT:
                        sys.exit()
                    case pygame.K_RIGHT:
                        snake.setDirection(Direction.RIGHT)
                    case pygame.K_LEFT:
                        snake.setDirection(Direction.LEFT)
                    case pygame.K_UP:
                        snake.setDirection(Direction.UP)
                    case pygame.K_DOWN:
                        snake.setDirection(Direction.DOWN)

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
