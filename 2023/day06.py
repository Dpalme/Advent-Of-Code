from sys import stdout
import re
import functools


def get_number_of_possible_wins(t, d):
    return sum((d / (i * (t - i))) < 1
               for i in range(d//t, t - 1))


def first_part(lns):
    races = zip(*map(
        lambda a: map(int, re.findall(r'\d+', a)),
        lns))
    return functools.reduce(
        lambda a, b: a*b,
        map(
            lambda r: get_number_of_possible_wins(*r),
            races
        )
    )


def second_part(lns):
    race = map(lambda line: int(''.join(re.findall(r'\d+', line))), lns)
    return get_number_of_possible_wins(*race)


with open('2023/inputs/day06.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 6\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
