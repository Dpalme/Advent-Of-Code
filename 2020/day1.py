from itertools import combinations
from sys import stdout


def first_part(numbers):
    for n in numbers:
        if 2020 - n in numbers:
            return n * (2020 - n)


def second_part(numbers):
    for n1, n2 in combinations(numbers, 2):
        if 2020 - n1 - n2 in numbers:
            return (2020 - n1 - n2) * n1 * n2


with open('2020/inputs/day1.txt', 'r') as inp:
    numbers = set([int(x) for x in inp.readlines()])
    stdout.write(f'Day 1\nFirst part: {first_part(numbers)}\n')
    stdout.write(f'Second part: {second_part(numbers)}\n')
