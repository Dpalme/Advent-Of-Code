from sys import stdout
from collections import defaultdict


def count_paths(curr='start', path={'start'}, dd=False):
    if curr == 'end':
        return 1
    return sum(
        count_paths(n, path, dd) if n.isupper() else (
            count_paths(n, path | {n}, dd) if n not in path else (
                count_paths(n, path, False) if dd and n != 'start' else
                    0
            )
        ) for n in caves[curr]
    )


with open('2021/inputs/day12.txt', 'r') as inp:
    caves = defaultdict(set)
    for f, t in map(lambda a: a.split('-'), inp.read().rsplit('\n')):
        caves[f].add(t)
        caves[t].add(f)
    stdout.write(f'Day 12\nFirst part: {count_paths()}\n')
    stdout.write(f'Second part: {count_paths(dd=True)}\n')
