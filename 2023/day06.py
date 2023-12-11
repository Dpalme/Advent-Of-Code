from sys import stdout
import re
import functools


def get_number_of_possible_wins(t, d):
    return sum((d / (i * (t - i))) < 1
               for i in range(1, t - 1))


def first_part(races):
    res = [*map(
        lambda r: get_number_of_possible_wins(*r),
        races
    )]
    print(res)
    return functools.reduce(
        lambda a, b: a*b,
        map(
            lambda r: get_number_of_possible_wins(*r),
            races
        )
    )


def second_part(races):
    race = map(int, functools.reduce(
        lambda a, b: (*(str(a[i])+str(b[i])
                        for i in (0, 1)),),
        races
    ))
    return get_number_of_possible_wins(*race)


with open('2023/inputs/day06.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    races = tuple(zip(*map(
        lambda a: map(int, re.findall(r'\d+', a)),
        lns)))
    stdout.write(f'Day 6\nFirst part: {first_part(races)}\n')
    stdout.write(f'Second part: {second_part(races)}\n')
