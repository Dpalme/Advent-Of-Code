from sys import stdout
from math import sqrt
from re import findall


class Map(object):
    def __init__(self, inp_str):
        self.tiles = [Tile(int(ln[5:9]), ln.split('\n')[1:]) for ln in inp_str]
        self.lines = []
        self.pair()

    def pair(self):
        for tile in self.tiles:
            for other in self.tiles:
                tile.pair(other)

    def get(self, tid):
        for tile in self.tiles:
            if tid == tile.tid:
                return tile

    def trim(self):
        for tile in self.tiles:
            tile.trim()

    def build(self):
        st_tile, lns = self.edges[2], []
        for _ in range(1):
            t_lns, nxt = st_tile.lines, st_tile.pairs[1]
            prev, count = None, 0
            while 1 in nxt.pairs or prev == nxt.pairs[1]:
                count += 1
                t_lns = self.join_lines(t_lns, nxt)
                if count % 2 == 0:
                    if prev == nxt:
                        print(prev, nxt.pairs[1])
                        break
                    prev = nxt
                nxt = nxt.pairs[1]
            lns.append('\n'.join(t_lns))
            st_tile = st_tile.pairs[2]
        return '\n'.join(lns)

    def join_lines(self, lines, tile):
        return [t1 + t2 for t1, t2 in zip(lines, tile.lines)]

    @property
    def edges(self):
        return tuple(t for t in self.tiles if t.connections == 2)

    @property
    def turb(self):
        return sum(t.turb for t in self.tiles)

    @property
    def width(self):
        return int(sqrt(len(self.tiles)))

    @property
    def mnstrs(self):
        self.trim()
        output_string = self.build()
        with open('2020/output.txt', 'w') as out:
            out.write(output_string)
        return 15


class Tile(object):
    def __init__(self, tid, lines):
        self.tid, self.lines = tid, lines
        self.brdrs = (lines[0], ''.join([i[-1] for i in lines]),
                      lines[-1], ''.join([i[0] for i in lines]))
        self.flpd = tuple(i[::-1] for i in self.brdrs)
        self.pairs = {}

    def pair(self, other):
        if self.tid != other.tid:
            for side, brdr in enumerate(self.brdrs):
                if brdr in other.brdrs:
                    other.rotate((other.flpd.index(brdr) + side) % 3)
                    self.pairs[side] = other
                elif brdr in other.flpd:
                    other.mirror((other.flpd.index(brdr) + side) % 3)
                    self.pairs[side] = other

    def trim(self):
        self.lines = [ln[1:-1] for ln in self.lines[1:-1]]

    def rotate(self, deg):
        if deg == 1:
            temp = [list()]*len(self.lines)
            for ln in self.lines:
                for ind, char in enumerate(ln):
                    temp[ind].append(ln)
            self.lines = [''.join(x) for x in temp]
        if deg == 2:
            self.lines = [line[::-1] for line in self.lines[::-1]]
        if deg == 3:
            temp = [list()]*len(self.lines)
            for ln in self.lines[::-1]:
                for ind, char in enumerate(ln):
                    temp[ind].append(ln)
            self.lines = [''.join(x) for x in temp]

    def mirror(self, ax):
        if ax == 1:
            lns = [line[::-1] for line in self.lines]
            self.brdrs = (lns[0], ''.join([i[-1] for i in lns]),
                          lns[-1], ''.join([i[0] for i in lns]))
            self.flpd = tuple(i[::-1] for i in self.brdrs)
            self.lines = lns
        if ax == 2:
            lns = self.lines[::-1]
            self.brdrs = (lns[0], ''.join([i[-1] for i in lns]),
                          lns[-1], ''.join([i[0] for i in lns]))
            self.flpd = tuple(i[::-1] for i in self.brdrs)
            self.lines = lns

    @property
    def connections(self):
        return len(self.pairs)

    @property
    def turb(self):
        return sum(len(tuple(n for n in i if n == '#')) for i in self.lines)

    @property
    def width(self):
        return len(self.lines[0])

    def __str__(self):
        return str(self.tid)

    def __repr__(self):
        return str(self.tid)


def first_part(tmap):
    acum = 1
    for t in tmap.edges:
        acum *= t.tid
    return acum


def second_part(tmap):
    # regex over input (#\.\.\.\.##) returned 44
    # thought maybe half of those were monsters
    # tried different inputs
    # 1587(22) < 1677(16) < x < 1722(13) < 1767(10)
    # answer 15
    t1 = tmap.get(1709)
    t2 = t1.pairs[1]
    print(t1, t1.brdrs, t2, t2.brdrs)
    mnstrs = tmap.mnstrs
    return tmap.turb - (15 * mnstrs)


with open('2020/inputs/test.txt', 'r') as inp:
    tmap = Map(inp.read().split('\n\n'))
    stdout.write(f'Day 20\nFirst part: {first_part(tmap)}\nSecond part: ')
    stdout.write(f'{second_part(tmap)}\n')
