from sys import stdout as std
from re import sub
from collections import defaultdict
dirs = {'w': (-1, 0), 'e': (1, 0), 'u': (0.5, -0.5),
        'b': (-0.5, -0.5), 'v': (0.5, 0.5), 'p': (-0.5, 0.5)}
dir_tup = ((-1, 0), (1, 0), (0.5, -0.5), (-0.5, -0.5), (0.5, 0.5), (-0.5, 0.5))


def first_part(inp_str):
    tiles = set()
    for line in inp_str:
        pos = (0, 0)
        for d in line:
            x, y = dirs[d]
            pos = (pos[0] + x, pos[1] + y)
        if pos in tiles:
            tiles.remove(pos)
        else:
            tiles.add(pos)
    return tiles


def second_part(tiles):
    def neighbors(crd):
        for dx, dy in dir_tup:
            yield crd[0] + dx, crd[1] + dy

    def switch(tiles):
        nei_tiles, n_tiles = defaultdict(int), set()
        for tile in tiles:
            for nei in neighbors(tile):
                nei_tiles[nei] += 1
        for coord, neis in nei_tiles.items():
            if neis == 2:
                n_tiles.add(coord)
            elif coord in tiles and neis == 1:
                n_tiles.add(coord)
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
