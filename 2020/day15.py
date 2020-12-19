from sys import stdout


def play(inp_str, stop):
    strt = [int(x) for x in inp_str.split(',')]
    spoke, numb = [0] * stop, strt[-1]
    for time, numb in enumerate(strt):
        spoke[numb] = time + 1
    for i in range(len(strt), stop):
        spoke[numb], numb = i, i - spoke[numb] if spoke[numb] != 0 else 0
    return numb


with open('2020/inputs/day15.txt', 'r') as inp:
    inp_str = inp.read()
    stdout.write(f'Day 15\nFirst part: {play(inp_str, 2020)}\n')
    stdout.write(f'Second part: {play(inp_str, 30000000)}\n')
