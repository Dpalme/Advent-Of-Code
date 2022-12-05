from sys import stdout
from itertools import product
from functools import reduce


class Cube(object):
    def __init__(self, x0, x1, y0, y1, z0, z1):
        super().__init__()
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1
        self.xr = set(range(x0, x1+1))
        self.yr = set(range(y0, y1+1))
        self.zr = set(range(z0, z1+1))
        self.verts = ((x0, x1), (y0, y1), (z0, z1))
        self.ranges = (self.xr, self.yr, self.zr)
        self.offset = 0

    @property
    def volume(self) -> int:
        return (abs(self.x1 - self.x0) * abs(self.y1 - self.y0) * abs(self.z1 - self.z0)) - self.offset

    def intersect(self, o):
        if ((o.x0 in self.xr or o.x1 in self.xr or self.x0 in o.xr or self.x1 in o.xr) and
            (o.y0 in self.yr or o.y1 in self.yr or self.y0 in o.yr or self.y1 in o.yr) and
                (o.z0 in self.zr or o.z1 in self.zr or self.z0 in o.zr or self.z1 in o.zr)):
            self.offset = len(set(product(*self.ranges)).intersection(product(*o.ranges)))
        return False


def first_part(lns):
    cubes = set()
    for ln in lns:
        op, ln = ln.split()
        [xr, yr, zr] = ln.split(',')
        xm, xM = map(int, xr[2:].split('..'))
        if xm < -50 or xM > 50:
            continue
        xr = range(xm, xM + 1)
        ym, yM = map(int, yr[2:].split('..'))
        if ym < -50 or yM > 50:
            continue
        yr = range(ym, yM + 1)
        zm, zM = map(int, zr[2:].split('..'))
        if zm < -50 or zM > 50:
            continue
        zr = range(zm, zM + 1)
        if op == 'on':
            cubes.update(product(xr, yr, zr))
        else:
            cubes.difference_update(product(xr, yr, zr))
    return len(cubes)


def second_part(lns):
    # cubes = set()
    # for ln in lns:
    #     op, ln = ln.split()
    #     [xr, yr, zr] = ln.split(',')
    #     cube = Cube(
    #         *map(int, xr[2:].split('..')),
    #         *map(int, yr[2:].split('..')),
    #         *map(int, zr[2:].split('..'))
    #     )
    #     if op == 'on':
    #         cubes.add(cube)
    #     else:
    #         pass
    # TODO
    return -1


with open('2021/inputs/day22.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 22\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part:\n2758514936282235\n{second_part(lns)}\n')
