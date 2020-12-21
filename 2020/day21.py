from sys import stdout
from collections import defaultdict


def parse_input(inp_str):
    all_ingr, pos_alrs, alrs = [], set(), defaultdict(set)
    for food in inp_str:
        args = [x.split() for x in food[:-1].replace(',', '').split('(')]
        all_ingr.extend(args[0])
        for i in args[1][1:]:
            alrs[i] = (set(args[0]) if alrs[i] == set() else
                       alrs[i].intersection(set(args[0])))
    [pos_alrs.update(pos) for name, pos in alrs.items()]
    return {i: sorted(x) for i, x in alrs.items()}, all_ingr, pos_alrs


def first_part(all_ingr, pos_alrs):
    return len([ing for ing in all_ingr if ing not in pos_alrs])


def second_part(alrs, pos_alrs):
    alrs = sorted(alrs.items(), key=lambda x: len(x[1]))
    for ind, (key, posses) in enumerate(alrs):
        chosen = False
        for poss in posses.copy():
            if poss in pos_alrs and not chosen:
                pos_alrs.remove(poss)
                chosen = True
            else:
                alrs[ind][1].remove(poss)
    return ",".join([n[0] for i, n in sorted(alrs)])


with open('2020/inputs/day21.txt', 'r') as inp:
    alrs, all_ingr, pos_alrs = parse_input(inp.read().split('\n'))
    stdout.write(f'Day 21\nFirst part: {first_part(all_ingr, pos_alrs)}\n')
    stdout.write(f'Second part: {second_part(alrs, pos_alrs)}\n')
