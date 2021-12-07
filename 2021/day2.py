from sys import stdout


def first_part(lns):
    x, y = 0, 0
    for cmd, v in (ln.split() for ln in lns):
        if (cmd == 'down'):
            y += int(v)
        elif cmd == 'up':
            y -= int(v)
        else:
            x += int(v)
    return x*y


def second_part(lns):
    x, y, aim = 0, 0, 0
    for cmd, v in (ln.split() for ln in lns):
        if (cmd == 'down'):
            aim += int(v)
        elif cmd == 'up':
            aim -= int(v)
        else:
            x += int(v)
            y += int(v) * aim
    return x*y


with open('2021/inputs/day2.txt', 'r') as inp:
    lns = inp.read().rsplit()
    stdout.write(f'Day 1\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
