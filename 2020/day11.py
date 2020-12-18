from itertools import product
from functools import lru_cache

dirs = set(product((-1, 0, 1), repeat=2)).difference(set([(0, 0)]))


def crowd(x, y, xm, ym, sts, line):
    if line:
        crowded = 0
        for i, j in dirs:
            dx, dy = x + i, y + j
            while 0 <= dx and dx < xm and 0 <= dy and dy < ym:
                if sts[dy][dx] != '.':
                    crowded += 1 if sts[dy][dx] == '#' else 0
                    break
                dx, dy = dx + i, dy + j
        return crowded
    else:
        return sum([sts[y+j][x+i] == '#' for i, j in dirs
                    if 0 <= x+i and x+i < xm and 0 <= y+j and y+j < ym])


def cycle(sts, xm, ym, line):
    copied = [[val for val in row] for row in sts]
    for y in range(ym):
        for x, seat in enumerate(sts[y]):
            crowded = crowd(x, y, xm, ym, sts, line)
            if seat == 'L' and crowded == 0:
                copied[y][x] = '#'
            elif seat == '#' and crowded > 3 + line:
                copied[y][x] = 'L'
    return copied


def setup(inp_str, line):
    sts = [[st for st in ln] for ln in inp_str.split('\n')]
    xm, ym, res = len(sts[0]), len(sts), None
    while res != sts:
        res, sts = sts, cycle(sts, xm, ym, line)
    return sum([sum([val == '#' for val in row]) for row in sts])


def first_part(inp_str):
    return setup(inp_str, False)


def second_part(inp_str):
    return setup(inp_str, True)


if __name__ == '__main__':
    with open('2020/inputs/day11.txt', 'r') as inp:
        input_string = inp.read()
        print('First part: %d' % first_part(input_string))
        print('Second part: %d' % second_part(input_string))
