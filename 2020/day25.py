from sys import stdout as std
from itertools import count
DIVIDER = 20201227


def first_part(door, key, sub):
    prod = 1
    for i in count():
        if prod == door:
            break
        prod = (prod*sub) % DIVIDER
    return pow(key, i, DIVIDER)


with open('2020/inputs/day25.txt', 'r') as inp:
    door, key = tuple(int(x) for x in inp.read().split('\n'))
    std.write('Day 25\nFirst part: ')
    std.write(f'{first_part(door, key, 7)}\n')
