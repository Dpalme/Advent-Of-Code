from sys import stdout
from functools import reduce


class Board(list):
    def __init__(self, lines):
        super().__init__()
        for y in lines.split('\n'):
            t = []
            for v in y.rsplit(' '):
                if v != '':
                    t.append(int(v) if v != '0' else -1)
            self.append(t)

    def sumall(self):
        return sum(sum((v if v != -1 else 0 for v in row)) for row in self)

    def update(self, n):
        for y, row in enumerate(self):
            for x, v in enumerate(row):
                if v == n:
                    self[y][x] = 0

    @property
    def done(self):
        if not reduce(lambda a, b: a*b, (sum(row) for row in self)):
            return True
        if not reduce(lambda a, b: a*b, (sum(row) for row in zip(*self))):
            return True
        return False
    

    def __str__(self) -> str:
        return "\n".join((" ".join((str(i).zfill(2) for i in row)) for row in self))


def first_part(turns, boards):
    boards = tuple(Board(lns) for lns in boards)
    for v in turns:
        v = v if v else -1
        for board in boards:
            board.update(v)
            if board.done:
                return board.sumall() * v


def second_part(turns, boards):
    boards = list(Board(lns) for lns in boards)
    c = 0
    for i, v in enumerate(turns):
        v = v if v else -1
        for board in boards.copy():
            board.update(v)
            if board.done:
                boards.remove(board)
        if len(boards) == 1:
            c = i
            break
    b = boards[0]
    while not b.done:
        b.update(turns[c])
        c+=1
    return b.sumall() * turns[c-1]


with open('2021/inputs/day4.txt', 'r') as inp:
    lns = inp.read().rsplit('\n\n')
    turns = tuple(map(int, lns[0].split(',')))
    stdout.write(f'Day 4\nFirst part: {first_part(turns, lns[1:])}\n')
    stdout.write(f'Second part: {second_part(turns, lns[1:])}\n')
