from sys import stdout
from functools import reduce
from collections import Counter

def first_part(lns): 
    bits = tuple(Counter(pos).most_common(1)[0][0] for pos in zip(*lns))
    gamma = int("".join(bits), base=2)
    epsilon = int("".join(("0" if i == "1" else "1") for i in bits), base=2)
    return gamma * epsilon


def second_part(lns):
    o, co2 = set(lns), set(lns)
    for ind in range(len(lns[0])):
        if len(o) > 1:
            bits = Counter(pos[ind] for pos in o).most_common(2)
            bit = bits[0][0] if bits[0][1] != bits[1][1] else "1"
            comp = filter(lambda x : x[ind] == bit, o)
            o.intersection_update(comp)
        if len(co2) > 1:
            bits = Counter(pos[ind] for pos in co2).most_common(2)
            bit = bits[1][0] if bits[0][1] != bits[1][1] else "0"
            comp = filter(lambda x : x[ind] == bit, co2)
            co2.intersection_update(comp)
    o = int("".join(o), base=2)
    co2 = int("".join(co2), base=2)
    return o * co2


with open('2021/inputs/day3.txt', 'r') as inp:
    lns = inp.read().rsplit()
    stdout.write(f'Day 1\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
