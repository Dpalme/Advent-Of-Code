from os import rename
from sys import stdout as std
from collections import defaultdict
from itertools import permutations


def first_part(reindeer, SECS=2503):
    return max((sum((secs * (SECS//len(secs) + 1))[:SECS])
                for secs in reindeer.values()))


def second_part(reindeer, SECS=2503):
    reind_p2 = {r: {'d': 0,
                    's': 0} for r in reindeer}
    for reind, route in reindeer.items():
        reindeer[reind] = (route * (SECS//len(route) + 1))
    for i in range(SECS):
        for r, route in reindeer.items():
            reind_p2[r]['d'] += route[i]
        maxd = max(x['d'] for x in reind_p2.values())
        for r in reindeer:
            reind_p2[r]['s'] += reind_p2[r]['d'] == maxd
    return max(x['s'] for x in reind_p2.values())


with open('2015/inputs/day14.txt', 'r') as inp:
    reindeer = {}
    for r in inp.read().split('\n'):
        r = r.split()
        reindeer[r[0]] = (*(int(r[3]),) * int(r[6]), *(0,) * int(r[-2]))
    std.write('Day 25\nFirst part: ')
    std.write(f'{first_part(reindeer, 1000)}\n')
    std.write('Second part: ')
    std.write(f'{second_part(reindeer)}\n')
