from functools import reduce
from itertools import product
from sys import stdout as std


def first_part(ingredients):
    return max(
        reduce(
            lambda a, b: (a * (a > 0)) * b,
            (
                (p[0] * i) + (p[1] * j) + (p[2] * k) + (p[3] * h)
                for p in tuple(zip(*ingredients))[:-1]
            )
        )
        for i, j, k, h in product(range(1, 97), repeat=len(ingredients))
        if i + j + k + h == 100
    )


def second_part(ingredients):
    calcs_100 = (
        cnf
        for cnf in product(range(1, 97), repeat=4)
        if (sum(cnf) == 100) and (
            sum(
                map(
                    lambda a: a[0]*a[1],
                    zip(cnf, tuple(zip(*ingredients))[-1])
                )
            ) == 500
        )
    )
    return max(
        reduce(
            lambda a, b: (a * (a > 0)) * b,
            (
                (p[0] * i) + (p[1] * j) + (p[2] * k) + (p[3] * h)
                for p in tuple(zip(*ingredients))[:-1]
            )
        )
        for i, j, k, h in calcs_100
    )


with open('2015/inputs/day15.txt', 'r') as inp:
    ingredients = []
    for i in inp.read().split('\n'):
        i = i.split()
        ingredients.append((int(i[2][:-1]), int(i[4][:-1]),
                            int(i[6][:-1]), int(i[8][:-1]), int(i[-1])))
    std.write('Day 25\nFirst part: ')
    std.write(f'{first_part(ingredients)}\n')
    std.write('Second part: ')
    std.write(f'{second_part(ingredients)}\n')
