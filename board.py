import random
from generic import Space


class Apple(Space):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Board:
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h
        self.apples: list[Apple] = []

    def check_collision(self, x: int, y: int, occupied_spaces: list[Space]) -> bool:
        for space in occupied_spaces:
            if x == space.x and y == space.y:
                return True

        return False

    def gen_apple(self, occupied_spaces: list[Space]):
        x = random.randint(0, self.w - 1)
        y = random.randint(0, self.h - 1)

        while self.check_collision(x, y, occupied_spaces):
            x = random.randint(0, self.w - 1)
            y = random.randint(0, self.h - 1)

        self.apples.append(Apple(x, y))

    def eat_apples(self, x: int, y: int, tailPieces: list[Space]) -> bool:
        for i in range(len(self.apples)):
            if self.apples[i].x == x and self.apples[i].y == y:
                occupied_spaces = tailPieces

                self.apples.pop(i)
                self.gen_apple(occupied_spaces)
                return True

        return False
