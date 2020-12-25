from itertools import product
from sys import stdout
from collections import defaultdict


def build_sts(lns):
    sts = {}
    for y, ln in enumerate(lns):
        for x, seat in enumerate(ln):
            if seat == 'L':
                sts[(x, y)] = 0
    return sts, len(lns[0]), len(lns)


def setup(sts, xm, ym, line):
    def cycle(sts):
        def neighbors(crd):
            for i, j in product((-1, 0, 1), repeat=2):
                if i == j == 0:
                    continue
                dx, dy = crd[0] + i, crd[1] + j
                while 0 <= dx < xm and 0 <= dy < ym:
                    if (dx, dy) in sts or not line:
                        yield dx, dy
                        break
                    dx, dy = dx + i, dy + j

        nei_tiles = defaultdict(int)
        for tile, val in sts.items():
            if val:
                for nei in neighbors(tile):
                    nei_tiles[nei] += 1
        n_sts = {}
        for crd, state in sts.items():
            if state:
                if nei_tiles[crd] > 3 + line:
                    n_sts[crd] = 0
                else:
                    n_sts[crd] = state
            elif nei_tiles[crd] == 0:
                n_sts[crd] = 1
            else:
                n_sts[crd] = state
        return n_sts
    res = None
    while res != sts:
        res, sts = sts, cycle(sts)
    return sum(sts.values())


with open('2020/inputs/day11.txt', 'r') as inp:
    sts, xm, ym = build_sts(inp.read().split('\n'))
    stdout.write('Day 11\nFirst part: ')
    stdout.write(f'{setup(sts.copy(), xm, ym, False)}\nSecond part: ')
    stdout.write(f'{setup(sts, xm, ym, True)}\n')
