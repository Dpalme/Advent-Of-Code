from itertools import product
from sys import stdout
from collections import defaultdict


def conway_cubes(lns, dims=3, cycs=6):
    dirs, cubes = set(product((-1, 0, 1), repeat=dims)), {}
    dirs.remove(((0,)*dims))
    for y, row in enumerate(lns):
        for x, cube in enumerate(row[:-1]):
            cubes[(x, y) + ((0,)*(dims-2))] = cube

    def cycle_cubes(c_cubes):
        active_cubes = defaultdict(int)

        for coord, val in c_cubes.items():
            if val == '#':
                for nei in [tuple(map(sum, zip(coord, b))) for b in dirs]:
                    active_cubes[nei] += 1

        n_map, count = {}, 0

        for coord, neis in active_cubes.items():
            current_state = '.' if coord not in c_cubes else c_cubes[coord]
            if current_state == '#' and not (2 <= neis <= 3):
                n_map[coord] = '.'
            elif current_state == '.' and neis == 3:
                n_map[coord] = '#'
            else:
                n_map[coord] = current_state

            count += n_map[coord] == '#'

        return n_map, count

    for i in range(cycs):
        cubes, active = cycle_cubes(cubes)
    return active


with open('2020/inputs/day17.txt', 'r') as inp:
    inp_str = inp.readlines()
    stdout.write(f'Day 17\nFirst part: {conway_cubes(inp_str)}\n')
    stdout.write(f'Second part: {conway_cubes(inp_str, 4)}\n')
