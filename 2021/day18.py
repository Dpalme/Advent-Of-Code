from sys import stdout
from math import ceil
from functools import reduce
from itertools import permutations
from copy import deepcopy

REDUCED = False


class Pair(object):
    def __init__(self, parent, a, b) -> None:
        super().__init__()
        self.parent = parent
        self.a, self.b = a, b
        self.s = (self.a, self.b)

    @property
    def magnitude(self):
        return (((self.a.magnitude if isinstance(self.a, Pair) else self.a) * 3) +
                ((self.b.magnitude if isinstance(self.b, Pair) else self.b) * 2))

    def del_child(self, c):
        if self.a == c:
            self.parent.cross_polinate(0, self, c.a)
            self.a = 0
            self.cross_polinate(1, self, c.b)
        else:
            self.cross_polinate(0, self, c.a)
            self.b = 0
            self.parent.cross_polinate(1, self, c.b)
        return True

    def cross_polinate(self, side, src, n):
        if side:
            if self.b == src:
                if self.parent is not None:
                    self.parent.cross_polinate(1, self, n)
            elif isinstance(self.b, Pair):
                self.b.rec_sum(0, n)
            else:
                self.b += n
        else:
            if self.a == src:
                if self.parent is not None:
                    self.parent.cross_polinate(0, self, n)
            elif isinstance(self.a, Pair):
                self.a.rec_sum(1, n)
            else:
                self.a += n

    def rec_sum(self, side, n):
        if side:
            if isinstance(self.b, int):
                self.b += n
            else:
                self.b.rec_sum(1, n)
        else:
            if isinstance(self.a, int):
                self.a += n
            else:
                self.a.rec_sum(0, n)

    def split(self, side):
        if side:
            self.b = Pair(self, self.b >> 1, ceil(self.b/2))
        else:
            self.a = Pair(self, self.a >> 1, ceil(self.a/2))
        return True

    def exp(self, d=0):
        if isinstance(self.a, Pair) and self.a.exp(d+1):
            return True
        if isinstance(self.b, Pair) and self.b.exp(d+1):
            return True
        if d >= 4:
            return self.parent.del_child(self)
        return False

    def rdc(self):
        if isinstance(self.a, Pair):
            if self.a.rdc():
                return True
        elif self.a > 9:
            return self.split(0)
        if isinstance(self.b, Pair):
            if self.b.rdc():
                return True
        elif self.b > 9:
            return self.split(1)
        return False

    def tree(self, space):
        sb = ""
        if isinstance(self.a, Pair):
            sb += f'[{self.a.tree(space+2)}]'
        else:
            sb += str(self.a)
        if isinstance(self.b, Pair):
            sb += f',[{self.b.tree(space+2)}]'
        else:
            sb += ',' + str(self.b)
        return sb

    def __repr__(self) -> str:
        return '[' + self.tree(1) + ']'


def add_pairs(a, b):
    root = Pair(None, a, b)
    a.parent = b.parent = root
    while True:
        while True:
            if not root.exp():
                break
        if not root.rdc():
            break
    return root


def first_part(pairs):
    return reduce(add_pairs, pairs).magnitude


def second_part(pairs):
    return max(
        map(
            lambda a: add_pairs(deepcopy(a[0]), deepcopy(a[1])).magnitude,
            permutations(pairs, 2)
        )
    )


def pair_builder(lstr, parent=None):
    root = Pair(parent, 0, 0)
    root.a = pair_builder(lstr[0], root) if isinstance(
        lstr[0], list) else lstr[0]
    root.b = pair_builder(lstr[1], root) if isinstance(
        lstr[1], list) else lstr[1]
    return root


with open('2021/inputs/day18.txt', 'r') as inp:
    pairs = list(map(pair_builder, map(eval, inp.read().rsplit('\n'))))
    stdout.write(f'Day 18\nFirst part: {first_part(deepcopy(pairs))}\n')
    stdout.write(f'Second part: {second_part(pairs)}\n')
