import random
from enum import Enum
from board import Board


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class TailPiece:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Snake:
    def __init__(self, board: Board, x: int = None, y: int = None):
        if x == None:
            self.x = random.randint(2, board.w - 2)
        else:
            self.x = x
        if y == None:
            self.y = random.randint(2, board.h - 2)
        else:
            self.y = y

        self.direction = Direction.RIGHT
        self.tailPieces: list[TailPiece] = [TailPiece(self.x - 1, self.y)]

    def setDirection(self, direction: Direction):
        self.direction = direction

    def move(self):
        if len(self.tailPieces) > 0:
            self.tailPieces[0].x = self.x
            self.tailPieces[0].y = self.y

        for i in range(1, len(self.tailPieces)):
            self.tailPieces[i].x = self.tailPieces[i - 1].x
            self.tailPieces[i].y = self.tailPieces[i - 1].y

        match self.direction:
            case Direction.RIGHT:
                self.x += 1
            case Direction.LEFT:
                self.x -= 1
            case Direction.DOWN:
                self.y += 1
            case Direction.UP:
                self.y -= 1
