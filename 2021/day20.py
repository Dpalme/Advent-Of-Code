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


def enhance(enh, img, ext, last_int):
    interior = {n for crd in last_int for n in neigh(crd)}
    def enh_algorithm(crds):
        return enh[int(''.join(ext if v not in last_int else (
                        '1' if v in img else '0') for v in crds), 2)]
    return {crd for crd in interior if enh_algorithm(neigh(crd))}, interior


def iterate(enh, img, iterations):
    last_ext = {n for crd in img for n in neigh(crd)}
    for i in range(iterations):
        ext = str(enh[0]) if not enh[0] or (i-1) % 2 == 0 else str(enh[-1])
        img, last_ext = enhance(enh, img, ext, last_ext)
    return len(img)


with open('2021/inputs/day20.txt', 'r') as inp:
    lns = inp.read().rsplit('\n\n')
    enh = tuple(('#' == c) << 0 for c in lns[0])
    img = set()
    for y, row in enumerate(lns[1].split('\n')):
        for x, v in enumerate(row):
            if v == '#':
                img.add((x, y))
    stdout.write(f'Day 20\nFirst part: {iterate(enh, img, 2)}\n')
    stdout.write(f'Second part: {iterate(enh, img, 50)}\n')
