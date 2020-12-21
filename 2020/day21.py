from sys import stdout
from re import search
from collections import defaultdict


def parse_input(inp_str):
    all_ingr, pos_alrs, alrs = [], set(), defaultdict(set)
    for food in inp_str:
        res = search(r'(.*)\s\(contains\s(.*)\)', food)
        ingr = res.group(1).split()
        all_ingr.extend(ingr)
        for alr in res.group(2).replace(',', '').split():
            if alrs[alr] == set():
                alrs[alr] = set(ingr)
            else:
                alrs[alr].intersection_update(set(ingr))
    [pos_alrs.update(pos) for name, pos in alrs.items()]
    return alrs, all_ingr, pos_alrs


def first_part(all_ingr, pos_alrs):
    return len([ing for ing in all_ingr if ing not in pos_alrs])


def second_part(alrs, pos_alrs):
    alrs = sorted(alrs.items(), key=lambda x: len(x[1]))
    for ind, (key, posses) in enumerate(alrs):
        chosen = False
        for poss in posses.copy():
            if poss in pos_alrs and not chosen:
                pos_alrs.discard(poss)
                chosen = True
            else:
                alrs[ind][1].discard(poss)
    return ",".join([n.pop() for i, n in sorted(alrs, key=lambda x: x[0])])


with open('2020/inputs/day21.txt', 'r') as inp:
    alrs, all_ingr, pos_alrs = parse_input(inp.read().split('\n'))
    stdout.write(f'Day 21\nFirst part: {first_part(all_ingr, pos_alrs)}\n')
    stdout.write(f'Second part: {second_part(alrs, pos_alrs)}\n')
