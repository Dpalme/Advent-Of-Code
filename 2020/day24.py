from sys import stdout as std
from re import sub
from collections import defaultdict
dirs = {'w': (-1, 0), 'e': (1, 0), 'u': (0.5, -0.5),
        'b': (-0.5, -0.5), 'v': (0.5, 0.5), 'p': (-0.5, 0.5)}
dir_tup = tuple(dirs.values())


def first_part(inp_str):
    tiles = {}
    for line in inp_str:
        pos = (0, 0)
        for d in line:
            pos = tuple(map(sum, zip(pos, dirs[d])))
        if pos in tiles:
            del tiles[pos]
        else:
            tiles[pos] = None
    return tiles


def second_part(tiles):
    def switch(tiles):
        nei_tiles, n_tiles = defaultdict(int), {}
        for tile in tiles:
            for nei in dir_tup:
                nei_tiles[tuple(map(sum, zip(tile, nei)))] += 1
        for coord, neis in nei_tiles.items():
            if neis == 2:
                n_tiles[coord] = None
            elif coord in tiles and neis == 1:
                n_tiles[coord] = None
        return n_tiles

    for _ in range(100):
        tiles = switch(tiles)
    return len(tiles)


with open('2020/inputs/day24.txt', 'r') as inp:
    tiles = first_part(sub('se', 'u', sub('sw', 'b', sub(
            'ne', 'v', sub('nw', 'p', inp.read())))).split('\n'))
    std.write('Day 24\nFirst part: ')
    std.write(f'{len(tiles)}\nSecond part: ')
    std.write(f'{second_part(tiles)}\n')
