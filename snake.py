import random
from enum import Enum
from board import Board
from generic import Space


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class TailPiece(Space):
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

        self.board = board
        self.direction = Direction.RIGHT
        self.moved_direction = self.direction
        self.tailPieces: list[TailPiece] = [
            TailPiece(self.x - 1, self.y), TailPiece(self.x - 2, self.y)]
        self.alive = True

    def setDirection(self, direction: Direction):
        if abs(self.moved_direction.value - direction.value) != 2:
            self.direction = direction

    def move(self):
        last_tailpiece = self.tailPieces[len(self.tailPieces) - 1]
        potential_growth = TailPiece(last_tailpiece.x, last_tailpiece.y)

        for i in range(len(self.tailPieces) - 1, 0, -1):
            self.tailPieces[i].x = self.tailPieces[i - 1].x
            self.tailPieces[i].y = self.tailPieces[i - 1].y

        self.tailPieces[0].x = self.x
        self.tailPieces[0].y = self.y

        match self.direction:
            case Direction.RIGHT:
                self.x += 1
            case Direction.LEFT:
                self.x -= 1
            case Direction.DOWN:
                self.y += 1
            case Direction.UP:
                self.y -= 1

        if self.x < 0 or self.x >= self.board.w or self.y < 0 or self.y >= self.board.h:
            self.alive = False

        for tailPiece in self.tailPieces + [potential_growth]:
            if self.x == tailPiece.x and self.y == tailPiece.y:
                self.alive = False

        if self.board.eat_apples(self.x, self.y, self.tailPieces):
            self.tailPieces.append(potential_growth)

        self.moved_direction = self.direction
