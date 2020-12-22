from itertools import product
from sys import stdout

DIRS = set(product((-1, 0, 1), repeat=2)).difference(set([(0, 0)]))


def setup(sts, line):
    xm, ym, res = len(sts[0]), len(sts), None

    def crowd(x, y, brkr):
        crowded = 0
        for i, j in DIRS:
            dx, dy = x + i, y + j
            while 0 <= dx < xm and 0 <= dy < ym:
                if sts[dy][dx] != '.' or not line:
                    crowded += sts[dy][dx] == '#'
                    if brkr and crowded >= 1:
                        return crowded
                    break
                dx, dy = dx + i, dy + j
        return crowded

    def cycle():
        copied, counter = [[val for val in row] for row in sts], 0
        for y in range(ym):
            for x, seat in enumerate(sts[y]):
                if seat != '.':
                    crowded = crowd(x, y, seat == 'L')
                    if seat == 'L' and crowded == 0:
                        copied[y][x] = '#'
                    elif seat == '#' and crowded > 3 + line:
                        copied[y][x] = 'L'
                    counter += copied[y][x] == '#'
        return copied, counter

    while res != sts:
        res, (sts, counter) = sts, cycle()
    return counter


with open('2020/inputs/day11.txt', 'r') as inp:
    sts = [[st for st in ln] for ln in inp.read().split('\n')]
    stdout.write('Day 11\nFirst part: ')
    stdout.write(f'{setup(sts, False)}\nSecond part: ')
    stdout.write(f'{setup(sts, True)}\n')
