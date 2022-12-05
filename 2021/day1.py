from sys import stdout


def first_part(numbers):
    rn = tuple(reversed(numbers))
    return sum(rn[i+1] < n for i, n in enumerate(rn[:-1]))


def second_part(ns):
    return first_part(tuple(n + ns[i+1] + ns[i+2] for i, n in enumerate(ns[:-2])))


with open('2021/inputs/day1.txt', 'r') as inp:
    numbers = tuple((int(x) for x in inp.readlines()))
    stdout.write(f'Day 1\nFirst part: {first_part(numbers)}\n')
    stdout.write(f'Second part: {second_part(numbers)}\n')
