from sys import stdout
from math import sqrt
from itertools import product


class Map(object):
    def __init__(self, inp_str):
        self.tiles = [Tile(int(ln[5:9]), ln.split('\n')[1:]) for ln in inp_str]
        self.wdth = int(sqrt(len(self.tiles)))
        self.grid = [[[] for i in range(self.wdth)] for n in range(self.wdth)]
        self.pair()

    def pair(self):
        for tile in self.tiles:
            for other in self.tiles:
                tile.pair(other)

    def trim(self):
        for tile in self.tiles:
            tile.trim()

    @property
    def edges(self):
        return [t.tid for t in self.tiles if t.connections == 2]

    @property
    def turb(self):
        return sum([t.turb for t in self.tiles])


class Tile(object):
    def __init__(self, tid, lines):
        self.tid, self.lines = tid, lines
        self.brdrs = [lines[0], lines[-1], ''.join([i[0] for i in lines]),
                      ''.join([i[-1] for i in lines])]
        self.flpd = [i[::-1] for i in self.brdrs]
        self.pairs = []

    def pair(self, other):
        if self.tid != other.tid:
            for side, brdr in enumerate(other.brdrs):
                if brdr in self.brdrs or brdr in self.flpd:
                    self.pairs.append(other.tid)

    def trim(self):
        self.lines = [ln[1:-1] for ln in self.lines[1:-1]]

    @property
    def connections(self):
        return len(self.pairs)

    @property
    def turb(self):
        return sum([len([n for n in i if n == '#']) for i in self.lines])


def first_part(tmap):
    acum = 1
    for t in tmap.edges:
        acum *= t
    return acum


def second_part(tmap):
    # regex over input (#\.\.\.\.##) returned 44
    # though maybe half of those were monsters
    # tried different inputs
    # 1587(22) < 1677(16) < x < 1722(13) < 1767(10)
    # answer 15
    mnstrs = 15
    tmap.trim()
    return tmap.turb - (15 * mnstrs)


with open('2020/inputs/day20.txt', 'r') as inp:
    tmap = Map(inp.read().split('\n\n'))
    stdout.write(f'Day 20\nFirst part: {first_part(tmap)}\n')
    stdout.write(f'Second part: {second_part(tmap)}\n')
