from functools import reduce
from sys import stdout

DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))


class XYPlane(dict):
    def __init__(self):
        super().__init__()

    def coord(self, x, y, val=None):
        coord = f'{x} {y}'
        if val is not None:
            self[coord] = val
        elif coord in self:
            return self[coord]
        return -1

    def __str__(self) -> str:
        sb = "  0123456789"
        for y in range(5):
            sb += f'\n{y} '
            for x in range(10):
                coord = f'{x} {y}'
                sb += str(self[coord]) if coord in self else '.'
        return sb + '\n'


def first_part(nMap):
    risk = 0

    def neighbors(x, y):
        for dx, dy in DIRS:
            coord = nMap.coord(x + dx, y + dy)
            if coord != -1:
                yield coord

    for coord, val in nMap.items():
        neighs = tuple(neighbors(*map(int, coord.split())))
        if val < min(neighs):
            risk += 1 + val
    return risk


def second_part(ns):
    basins = []

    def neighbors(x, y):
        for dx, dy in DIRS:
            coord = nMap.coord(x + dx, y + dy)
            if coord != -1:
                yield coord

    def bneighbors(x, y):
        for dx, dy in DIRS:
            val = nMap.coord(x + dx, y + dy)
            if val != -1:
                yield (x + dx, y + dy), val

    def dfs(x, y, basin):
        val, coord = nMap.coord(x, y), f'{x} {y}'
        if val == 9 or coord in basin:
            return basin
        basin.add(coord)
        for c, v in bneighbors(x, y):
            if (v >= val) and f'{c[0]} {c[1]}' not in basin:
                basin.update(dfs(*c, basin))
        return basin

    for coord, val in nMap.items():
        if val < min(neighbors(*map(int, coord.split()))):
            basins.append(dfs(*map(int, coord.split()), set()))
    return reduce(lambda a, b: a*b, map(len, sorted(basins, key=len)[-3:]))


with open('2021/inputs/day9.txt', 'r') as inp:
    nMap = XYPlane()
    lns = inp.readlines()
    for y, row in enumerate(lns):
        for x, v in enumerate(row.strip()):
            nMap.coord(x, y, int(v))
    stdout.write(f'Day 9\nFirst part: {first_part(nMap)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
