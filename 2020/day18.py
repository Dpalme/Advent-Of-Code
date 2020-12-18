from re import sub


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
    return sum([evaluate(ln.replace('*', '-')) for ln in inp_str.split('\n')])


def second_part(inp_str):
    return sum([evaluate(ln.replace('*', '-').replace('+', '*'))
               for ln in inp_str.split('\n')])

with open('2020/inputs/day18.txt', 'r') as inp:
    inp_str = inp.read()
    print('First part: %d' % first_part(inp_str))
    print('Second part: %d' % second_part(inp_str))
