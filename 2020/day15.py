from sys import stdout


def first_part(input_data):
    spoke = {int(numb): time + 1 for time,
             numb in enumerate(input_data.split(','))}
    numb = list(spoke.keys())[-1]
    for i in range(len(spoke), 2020):
        spoke[numb], numb = (i, i - spoke[numb]) if numb in spoke else (i, 0)
    return numb


def second_part(input_data):
    spoke = {int(numb): time + 1 for time,
             numb in enumerate(input_data.split(','))}
    numb = list(spoke.keys())[-1]
    for i in range(len(spoke), 30000000):
        spoke[numb], numb = (i, i - spoke[numb]) if numb in spoke else (i, 0)
    return numb


with open('2020/inputs/day15.txt', 'r') as inp:
    inp_str = inp.read()
    stdout.write(f'Day 15\nFirst part: {first_part(inp_str)}\n')
    stdout.write(f'Second part: {second_part(inp_str)}\n')
