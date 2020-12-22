from itertools import combinations
from sys import stdout


def first_part(numbers):
    for n in numbers:
        i = 2020 - n
        if i in numbers:
            return n * i


def second_part(numbers):
    for n1, n2 in combinations(numbers, 2):
        i = 2020 - n1 - n2
        if i in numbers:
            return i * n1 * n2


with open('2020/inputs/day1.txt', 'r') as inp:
    numbers = set((int(x) for x in inp.readlines()))
    stdout.write(f'Day 1\nFirst part: {first_part(numbers)}\n')
    stdout.write(f'Second part: {second_part(numbers)}\n')
