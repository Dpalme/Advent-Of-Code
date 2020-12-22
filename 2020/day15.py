from sys import stdout


def play(strt, stop1, stop):
    spoke, numb = [0] * stop, strt[-1]
    for time, numb in enumerate(strt):
        spoke[numb] = time + 1
    for i in range(len(strt), stop1):
        spoke[numb], numb = i, i - spoke[numb] if spoke[numb] != 0 else 0
    back = numb
    for i in range(stop1, stop):
        spoke[numb], numb = i, i - spoke[numb] if spoke[numb] != 0 else 0
    return back, numb


with open('2020/inputs/day15.txt', 'r') as inp:
    strt = tuple(int(x) for x in inp.read().split(','))
    p1, p2 = play(strt, 2020, 30000000)
    stdout.write(f'Day 15\nFirst part: {p1}\n')
    stdout.write(f'Second part: {p2}\n')
