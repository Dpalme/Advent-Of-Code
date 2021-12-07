from sys import stdout as std
from collections import defaultdict
from itertools import permutations


def first_part(people):
    n = len(people)
    return max((sum((people[p][comb[(i - 1) % n]] + people[p][comb[(i + 1) % n]]
                     for i, p in enumerate(comb)))
                for comb in permutations(people.keys(), n)))


def second_part(people):
    people['me'] = {p: 0 for p in people}
    for p in people:
        people[p]['me'] = 0
    n = len(people)
    return max((sum((people[p][comb[(i - 1) % n]] + people[p][comb[(i + 1) % n]]
                     for i, p in enumerate(comb)))
                for comb in permutations(people.keys(), n)))

with open('2015/inputs/day13.txt', 'r') as inp:
    people = defaultdict(dict)
    for x in inp.read().replace('.', '').split('\n'):
        p = x.split()
        people[p[0]][p[-1]] = int(p[3]) * (-1 if p[2] == 'lose' else 1)
    std.write('Day 25\nFirst part: ')
    std.write(f'{first_part(people)}\n')
    std.write('Second part: ')
    std.write(f'{second_part(people)}\n')
