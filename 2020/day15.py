from sys import stdout


def play(inp_str, stop):
    spoke = {int(numb): time + 1 for time, numb in enumerate(inp_str.split(','))}
    numb = list(spoke.keys())[-1]
    for i in range(len(spoke), stop):
        spoke[numb], numb = (i, i - spoke[numb]) if numb in spoke else (i, 0)
    return numb


with open('2020/inputs/day15.txt', 'r') as inp:
    inp_str = inp.read()
    stdout.write(f'Day 15\nFirst part: {play(inp_str, 2020)}\n')
    stdout.write(f'Second part: {play(inp_str, 30000000)}\n')
