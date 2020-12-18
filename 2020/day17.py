from itertools import product
from copy import deepcopy


def first_part(inp_data, cycs):
    lns = inp_data.split('\n')
    size, zm = cycs*2+len(lns), 2*cycs + 1
    spr = range(size)
    empty = [[[0 for x in spr] for y in spr] for z in range(zm)]
    cubes = deepcopy(empty)
    for x, y in product(range(len(lns)), repeat=2):
        cubes[cycs][cycs+y][cycs+x] = 1 if lns[y][x] == '#' else 0
    for i in range(cycs):
        cpy = deepcopy(empty)
        for z in range(zm):
            for x, y in product(range(size), repeat=2):
                stt = cubes[z][y][x]
                nei = sum([cubes[z+k][y+j][x+i]
                           for i, j, k in product((-1, 0, 1), repeat=3) if (
                    0 <= x+i and x+i < size) and (
                    0 <= y+j and y+j < size) and (
                    0 <= z+k and z+k < zm)]) - stt

                cpy[z][y][x] = stt
                if stt and not (nei == 2 or nei == 3):
                    cpy[z][y][x] = 0
                elif not stt and nei == 3:
                    cpy[z][y][x] = 1
        cubes = cpy
    return 2 * sum([sum([sum(row) for row in slc])
                   for slc in cubes[:cycs]]) + sum([sum(row)
                                                   for row in cubes[cycs]])


def second_part(inp_data, cycs):
    lns = inp_data.split('\n')
    size, zm = cycs*2+len(lns), 2*cycs + 1
    spr = range(size)
    empty = [[[[0 for x in spr] for y in spr]
              for z in range(zm)] for w in range(zm)]
    cubes = deepcopy(empty)
    for x, y in product(range(len(lns)), repeat=2):
        cubes[cycs][cycs][cycs+y][cycs+x] = 1 if lns[y][x] == '#' else 0
    for i in range(cycs):
        cpy = deepcopy(empty)
        for z, w in product(range(zm), repeat=2):
            for x, y in product(range(size), repeat=2):
                stt = cubes[w][z][y][x]
                nei = sum([cubes[w+l][z+k][y+j][x+i]
                           for i, j, k, l in product((-1, 0, 1), repeat=4) if (
                    0 <= x+i and x+i < size) and (
                    0 <= y+j and y+j < size) and (
                    0 <= z+k and z+k < zm) and (
                        0 <= w+l and w+l < zm)]) - stt

                cpy[w][z][y][x] = stt
                if stt and not (nei == 2 or nei == 3):
                    cpy[w][z][y][x] = 0
                elif not stt and nei == 3:
                    cpy[w][z][y][x] = 1
        cubes = cpy
    return sum([sum([sum([sum(row) for row in slc])
                     for slc in slc3]) for slc3 in cubes])


if __name__ == '__main__':
    with open('2020/inputs/day17.txt', 'r') as inp:
        inp_str = inp.read()
        print('First part: %d' % first_part(inp_str, 6))
        print('Second part: %d' % second_part(inp_str, 6))
