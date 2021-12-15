from sys import stdout
from math import ceil
from itertools import product

def cycle(letters, start, rules, iterations):
    for step in range(iterations):
        result = start.copy()
        for pair, v in start.items():
            if v and pair in rules:
                result[pair[0] + rules[pair]] += v
                result[pair] -= v
                result[rules[pair] + pair[1]] += v
        start = result
    final_count = {l: 0 for l in letters}
    for k, v in start.items():
        final_count[k[0]] += v / 2
        final_count[k[1]] += v / 2
    fcv = final_count.values()
    return ceil(max(fcv) - min(fcv))



with open('2021/inputs/day14.txt', 'r') as inp:
    start, rules = inp.read().rsplit('\n\n')
    rules = {a.split(' -> ')[0]: a.split(' -> ')[1] for a in rules.split('\n')}
    letters = set("".join((k + v for k,v in rules.items())))
    pairs = {"".join(k): 0 for k in product(letters, repeat=2)}
    for pair in zip(start[:-1], start[1:]):
        pairs["".join(pair)] += 1
    stdout.write(f'Day 14\nFirst part: {cycle(letters, pairs, rules, 10)}\n')
    stdout.write(f'Second part: {cycle(letters, pairs, rules, 40)}\n')
