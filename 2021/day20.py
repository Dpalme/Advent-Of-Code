from sys import stdout
from functools import lru_cache
from collections import defaultdict

DIRS = (
    (-1, -1), (0, -1), (1, -1),
    (-1,  0), (0,  0), (1,  0),
    (-1,  1), (0,  1), (1,  1),
)


@lru_cache
def neigh(crd):
    return tuple((crd[0]+dx, crd[1]+dy) for dx, dy in DIRS)


def enhance(enh, img, ext):
    new_img = defaultdict(lambda:ext)
    interior = {n for crd in img for n in neigh(crd)}

    def enh_algorithm(crds):
        n = 0
        for v in crds:
            n = n + img[v]
            n = n << 1
        return enh[n >> 1]

    for crd in interior:
        new_img[crd] = enh_algorithm(neigh(crd))
    return new_img


def iterate(enh, img, iterations):
    for i in range(iterations):
        img = enhance(enh, img, enh[0] if not enh[0] or i%2==0 else enh[-1])
    return sum(img.values())


with open('2021/inputs/day20.txt', 'r') as inp:
    lns = inp.read().rsplit('\n\n')
    enh = tuple('#' == c for c in lns[0])
    img = defaultdict(lambda:0)
    for y, row in enumerate(lns[1].split('\n')):
        for x, v in enumerate(row):
            if v == '#':
                img[(x, y)] = 1
    stdout.write(f'Day 20\nFirst part: {iterate(enh, img, 2)}\n')
    stdout.write(f'Second part: {iterate(enh, img, 50)}\n')
