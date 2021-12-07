from sys import stdout


def first_part(pos):
    i = sorted(pos)[len(pos)//2]
    return sum(
        map(
            lambda a: abs(a-i), pos
        )
    )


def second_part(pos):
    i = sum(pos) // len(pos)
    return sum(
        map(
            lambda a: (abs(a-i) * (abs(a-i) + 1)) // 2, pos
        )
    )


with open('2021/inputs/day7.txt', 'r') as inp:
    pos = tuple(map(int, inp.read().split(',')))
    stdout.write(f'Day 7\nFirst part: {first_part(pos)}\n')
    stdout.write(f'Second part: {second_part(pos)}\n')
