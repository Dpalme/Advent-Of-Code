from sys import stdout


def first_part(inp_str):
    arr, acs = set(int(nbr) for nbr in inp_str.split('\n')), [0, 0, 0, 1]
    for ad in arr:
        acs[ad - acs[0]], acs[0] = acs[ad - acs[0]] + 1, ad
    return acs[1] * acs[3]


def second_part(inp_str):
    arr = sorted([0] + [int(nbr) for nbr in inp_str.split('\n')])
    acs = [1] + [0 for i in range(len(arr) - 1)]
    for x, ax in enumerate(arr):
        acs[x] += sum(acs[y] for y in range(x-3, x) if ax-arr[y] <= 3)
    return acs[-1]


with open('2020/inputs/day10.txt', 'r') as inp:
    inp_str = inp.read()
    stdout.write(f'Day 10\nFirst part: {first_part(inp_str)}\n')
    stdout.write(f'Second part: {second_part(inp_str)}\n')
