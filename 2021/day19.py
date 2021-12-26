from sys import stdout
from itertools import combinations
from functools import lru_cache, reduce

@lru_cache(None)
def manh(a, b):
    return sum(map(lambda a: (a[1]-a[0])**2, zip(a, b)))


@lru_cache(None)
def scanner_profile(s):
    return {manh(a, b) for a in s for b in s if b != a}


def first_part(scns):
    # TODO
    return -1


def second_part(ns):
    # TODO
    return -1


with open('2021/inputs/day19.txt', 'r') as inp:
    scnlns = inp.read().rsplit('\n\n')
    scanners = tuple(tuple(eval(f'({a})') for a in lns.split('\n')[1:]) for lns in scnlns)
    stdout.write(f'Day 19\nFirst part: {first_part(scanners)}\n')
    stdout.write(f'Second part: {second_part(scanners)}\n')
