from sys import stdout


def play(strt, stop):
    spoke, numb = [0] * stop, strt[-1]
    for time, numb in enumerate(strt):
        spoke[numb] = time + 1
    for i in range(len(strt), stop):
        spoke[numb], numb = i, i - spoke[numb] if spoke[numb] != 0 else 0
    return numb


with open('2020/inputs/day15.txt', 'r') as inp:
    strt = tuple(int(x) for x in inp.read().split(','))
    stdout.write(f'Day 15\nFirst part: {play(strt, 2020)}\n')
    stdout.write(f'Second part: {play(srtr, 30000000)}\n')
