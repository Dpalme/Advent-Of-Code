from re import sub
from sys import stdout


class int2(int):
    def __sub__(self, other):
        return int2(int(self) * other)

    def __add__(self, other):
        return int2(int(self) + other)

    def __mul__(self, other):
        return int2(int(self) + other)


def evaluate(exp):
    return eval(sub(r"(\d+)", r"int2(\1)", exp))


def first_part(inp_str):
    return sum(evaluate(ln) for ln in lns)


def second_part(inp_str):
    return sum(evaluate(sub(r'[+]', '*', ln)) for ln in lns)


with open('2020/inputs/day18.txt', 'r') as inp:
    inp_str = sub(r'[*]', '-', inp.read())
    lns = inp_str.split('\n')
    stdout.write(f'Day 18\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
