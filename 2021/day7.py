from sys import stdout


def sumdig(n):
    return (n * (n + 1)) / 2


def first_part(pos):
    return min(
        sum(
            map(
                lambda a: abs(a-i), pos
            )
        )
        for i in range(min(pos), max(pos) + 1)
    )


def second_part(ns):
    return int(min(
        sum(
            map(
                lambda a: sumdig(abs(a-i)),
                pos
            )
        )
        for i in range(min(pos), max(pos) + 1)
    ))


with open('2021/inputs/day7.txt', 'r') as inp:
    pos = tuple(map(int, inp.read().split(',')))
    stdout.write(f'Day 7\nFirst part: {first_part(pos)}\n')
    stdout.write(f'Second part: {second_part(pos)}\n')
