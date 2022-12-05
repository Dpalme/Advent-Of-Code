from sys import stdout


class XYPlane(dict):
    def __init__(self):
        super().__init__()

    def touch(self, crd):
        if crd in self:
            self[crd] += 1


def cycle(octupi):
    flashed = set()

    def neighbors(x, y):
        return((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1))

    def flash(crd):
        flsh = 1
        flashed.add(crd)
        for ncoord in neighbors(*crd):
            if ncoord not in octupi:
                continue
            octupi[ncoord] += 1
            if ncoord in octupi and octupi[ncoord] > 9 and ncoord not in flashed:
                flash(ncoord)
        return flsh

    for crd in octupi:
        if octupi[crd] == 9 and crd not in flashed:
            flash(crd)
        else:
            octupi[crd] += 1

    for coord in flashed:
        octupi[coord] = 0

    return octupi, len(flashed)


def first_part(octupi):
    flashes = 0
    for _ in range(1, 101):
        octupi, flashs = cycle(octupi)
        flashes += flashs
    return flashes


def second_part(octupi):
    for i in range(1, 30000):
        octupi, flashd = cycle(octupi)
        if flashd == 100:
            return 100 + i


with open('2021/inputs/day11.txt', 'r') as inp:
    nMap = XYPlane()
    for y, row in enumerate(inp.read().rsplit('\n')):
        for x, v in enumerate(row):
            nMap[(x, y)] = int(v)
    stdout.write(f'Day 11\nFirst part: {first_part(nMap)}\n')
    stdout.write(f'Second part: {second_part(nMap)}\n')
