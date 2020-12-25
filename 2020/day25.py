from sys import stdout as std
DIVIDER = 20201227


def get_cyc(i, sub):
    x, count = 1, 0
    while x != i:
        x *= sub
        x %= DIVIDER
        count += 1
    return count


def get_en_key(sub, cyc):
    x = 1
    for _ in range(cyc):
        x *= sub
        x %= DIVIDER
    return x


def first_part(door, key, sub):
    d_loop_s = get_cyc(key, sub)
    en_key = get_en_key(door, d_loop_s)
    return en_key


with open('2020/inputs/day25.txt', 'r') as inp:
    door, key = tuple(int(x) for x in inp.read().split('\n'))
    std.write('Day 25\nFirst part: ')
    std.write(f'{first_part(door, key, 7)}\n')
