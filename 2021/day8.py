from functools import reduce
from sys import stdout

'''
1 - cf
7 - acf
4 - bcdf
8 - abcdefg
0 - abcefg
6 - abdefg
9 - abcdfg
2 - acdeg
3 - acdfg
5 - abdfg


0 - abcefg
6 - abdfeg
9 - abcdfg
2 - ce
3 - cf
5 - f
'''


def first_part(lns):
    return sum(sum(map(lambda a: len(a) in (4, 7, 3, 2), ln.split(' | ')[1].split())) for ln in lns)


def second_part(lns):
    total = 0
    for ln in lns:
        p1, p2 = ln.split(' | ')
        all_digits = p1.split()
        dt = {len(v): set(v) for v in all_digits}
        a = dt[3].difference(dt[2])
        dg = reduce(
            lambda a, b: a.intersection(b),
            map(
                set,
                filter(
                    lambda a: len(a) == 5,
                    all_digits
                )
            )
        ).difference(dt[3])
        bd = dt[4].difference(dt[2])
        d = bd.intersection(dg)
        b = bd.difference(d)
        g = dt[7].difference(*dt[2], *bd, *a).intersection(dg)
        f = tuple(filter(
            lambda a: len(a) == 2,
            map(
                lambda a: a.difference(b, d, g),
                map(
                    set,
                    filter(
                        lambda a: len(a) == 5,
                        all_digits
                    )
                )
            )
        ))[0].difference(a)
        c = dt[2].difference(f)
        e = dt[7].difference(a, b, c, d, f, g)

        trans = [set().union(*a, *b, *c, *e, *f, *g),
                 set().union(*dt[2], ),
                 set().union(*a, *c, *d, *e, *g),
                 set().union(*a, *c, *d, *f, *g),
                 set().union(*dt[4], ),
                 set().union(*a, *b, *d, *f, *g),
                 set().union(*a, *b, *d, *e, *f, *g),
                 set().union(*dt[3], ),
                 set().union(*dt[7], ),
                 set().union(*a, *b, *c, *d, *f, *g)]
        total += int("".join(
            map(
                lambda a: str(trans.index(a)),
                (set(a) for a in p2.split())
            )
        ))
    return total


with open('2021/inputs/day8.txt', 'r') as inp:
    lns = inp.readlines()
    stdout.write(f'Day 8\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
