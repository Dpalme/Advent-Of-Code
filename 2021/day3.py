from sys import stdout
from collections import Counter

def first_part(lns): 
    bits = tuple(Counter(pos).most_common(1)[0][0] for pos in zip(*lns))
    gamma = int("".join(bits), base=2)
    epsilon = gamma ^ (2 ** len(bits)) - 1
    return gamma * epsilon


def second_part(lns):
    o, co2 = set(lns), set(lns)
    for ind in range(len(lns[0])):
        lo, lco = len(o) > 1, len(co2) > 1
        if not (lo or lco):
            break
        if lo:
            bits = Counter(pos[ind] for pos in o).most_common(2)
            bit = bits[0][0] if bits[0][1] != bits[1][1] else "1"
            o.intersection_update(filter(lambda x : x[ind] == bit, o))
        if lco:
            bits = Counter(pos[ind] for pos in co2).most_common(2)
            bit = bits[1][0] if bits[0][1] != bits[1][1] else "0"
            co2.intersection_update(filter(lambda x : x[ind] == bit, co2))
    return int("".join(o), base=2) * int("".join(co2), base=2)


with open('2021/inputs/day3.txt', 'r') as inp:
    lns = inp.read().rsplit()
    stdout.write(f'Day 3\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
