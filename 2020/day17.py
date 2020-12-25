from itertools import product
from sys import stdout
from collections import defaultdict


def conway_cubes(lns, dims=3, cycs=6):
    cubes = set()
    for y, row in enumerate(lns):
        for x, cube in enumerate(row):
            if cube == '#':
                cubes.add((x, y) + (0,)*(dims-2))

    def neighbors(crd):
        if dims == 4:
            for dx, dy, dz, dw in product([-1, 0, 1], repeat=dims):
                if (dx, dy, dz, dw) != (0, 0, 0, 0):
                    yield crd[0] + dx, crd[1] + dy, crd[2] + dz, crd[3] + dw
        else:
            for dx, dy, dz in product([-1, 0, 1], repeat=dims):
                if (dx, dy, dz) != (0, 0, 0):
                    yield crd[0] + dx, crd[1] + dy, crd[2] + dz

    def cycle_cubes(c_cubes):
        active_cubes = defaultdict(int)
        for coord in c_cubes:
            for nei in neighbors(coord):
                active_cubes[nei] += 1

        n_map = set()
        for coord, neis in active_cubes.items():
            if coord in c_cubes:
                if 2 <= neis <= 3:
                    n_map.add(coord)
            elif neis == 3:
                n_map.add(coord)
        return n_map

    for i in range(cycs):
        cubes = cycle_cubes(cubes)
    return len(cubes)


with open('2020/inputs/day17.txt', 'r') as inp:
    inp_str = inp.read().split('\n')
    stdout.write(f'Day 17\nFirst part: {conway_cubes(inp_str)}\n')
    stdout.write(f'Second part: {conway_cubes(inp_str, 4)}\n')
