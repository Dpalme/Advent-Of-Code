from sys import stdout
from itertools import product


class Probe(dict):
    def __init__(self, vx, vy, t) -> None:
        super().__init__()
        self[0] = 0
        self[1] = 0
        self[2] = vx
        self[3] = vy
        self[4] = t
        self[5] = 0
        self.xr = range(min(self[4][0]), max(self[4][0]) + 1)
        self.yr = range(min(self[4][1]), max(self[4][1]) + 1)

    @property
    def status(self):
        if self[0] in self.xr and self[1] in self.yr:
            return 1
        elif self[0] > max(self[4][0]) or (self[1] < min(self[4][1]) and self[3] < 0):
            return -1
        return 0

    def update(self):
        self[0] += self[2]
        self[1] += self[3]
        self[2] += 1 * (self[2] < 0) - 1*(self[2] > 0)
        self[3] -= 1
        self[5] = self[5] * (self[1] <= self[5]) + \
            self[1] * (self[1] > self[5])

    def calc(self):
        return self[5] * self.status

    def compute(self):
        while self.status == 0:
            self.update()
        return self


def first_part(probes):
    return max(
        map(
            lambda a: a.calc(),
            probes
        )
    )


def second_part(probes):
    return len(
        tuple(
            filter(
                lambda a: a.status > 0,
                probes
            )
        )
    )


with open('2021/inputs/day17.txt', 'r') as inp:
    t = tuple(
        map(
            lambda a: tuple(
                map(
                    int,
                    a[2:].split('..')
                )
            ),
            inp.read()[13:].split(', ')
        )
    )
    probes = tuple(
        map(
            lambda p: Probe(*p, t).compute(),
            product(
                range(
                    -max(
                        map(
                            abs,
                            t[1]
                        )
                    ) - 1,
                    max(t[0]) + 1
                ),
                range(
                    -max(
                        map(
                            abs,
                            t[1]
                        )
                    ),
                    max(
                        map(
                            abs,
                            t[1]
                        )
                    ) + 1
                )
            )
        )
    )
    stdout.write(f'Day 17\nFirst part: {first_part(probes)}\n')
    stdout.write(f'Second part: {second_part(probes)}\n')
