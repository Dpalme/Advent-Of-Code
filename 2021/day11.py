from sys import stdout


class XYPlane(dict):
    def __init__(self):
        super().__init__()

    def crd(self, crd, val=None):
        if val is not None:
            self[crd] = val
        elif crd in self:
            return self[crd]
        return -1

    def coord(self, x, y, val=None):
        coord = (x, y)
        if val is not None:
            self[coord] = val
        elif coord in self:
            return self[coord]
        return -1

    def touch(self, crd, src=None):
        if src == (2,1):
            print(src, '->', crd)
        if crd in self:
            self[crd] += 1

    def __str__(self) -> str:
        sb = ""
        for y in range(10):
            sb += "".join((str(self[(x, y)]) for x in range(10))) + '\n'
        return sb + '\n'


def first_part(octupi):
    flashes = 0

    def neighbors(x, y):
        return((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1))

    def cycle(octupi):
        flashs = 0
        flashed = set()

        def flash(crd):
            flsh = 1
            flashed.add(crd)
            for ncoord in neighbors(*crd):
                octupi.touch(ncoord)
                if octupi.crd(ncoord) > 9 and ncoord not in flashed:
                    flsh += flash(ncoord)
            return flsh

        for crd in octupi:
            if octupi.crd(crd) == 9 and crd not in flashed:
                flashs += flash(crd)
            else:
                octupi.touch(crd)

        for coord in flashed:
            octupi.crd(coord, 0)

        return octupi, flashs

    for i in range(1, 101):
        octupi, flashs = cycle(octupi)
        flashes += flashs
    return flashes


def second_part(octupi):

    def neighbors(x, y):
        return((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1))

    def cycle(octupi):
        flashed = set()

        def flash(crd):
            flashed.add(crd)
            for ncoord in neighbors(*crd):
                octupi.touch(ncoord)
                if octupi.crd(ncoord) > 9 and ncoord not in flashed:
                    flash(ncoord)

        for crd in octupi:
            if octupi.crd(crd) == 9 and crd not in flashed:
                flash(crd)
            else:
                octupi.touch(crd)

        for coord in flashed:
            octupi.crd(coord, 0)

        return octupi, len(flashed)

    for i in range(1, 30000):
        octupi, flashd = cycle(octupi)
        if flashd == 100:
            return 100 + i


with open('2021/inputs/day11.txt', 'r') as inp:
    nMap = XYPlane()
    lns = inp.readlines()
    for y, row in enumerate(lns):
        for x, v in enumerate(row.strip()):
            nMap.coord(x, y, int(v))
    stdout.write(f'Day 9\nFirst part: {first_part(nMap)}\n')
    stdout.write(f'Second part: {second_part(nMap)}\n')
