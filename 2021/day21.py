from sys import stdout
from itertools import product
from functools import lru_cache, reduce

DIRAC_SUMS = tuple(sum(rolls) for rolls in product((1, 2, 3), repeat=3))
BOARD = (10, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def first_part(p1, p2):
    scores = [0, 0]
    dice = (100, *range(1, 100))
    i = 1
    while scores[0] < 1000 and scores[1] < 1000:
        n = (dice[i % 100], dice[(i+1) % 100], dice[(i+2) % 100])
        p1 = BOARD[(p1+sum(n)) % 10]
        scores[0] += p1
        i += 3
        if scores[0] >= 1000:
            break
        n = (dice[i % 100], dice[(i+1) % 100], dice[(i+2) % 100])
        p2 = BOARD[(p2+sum(n)) % 10]
        scores[1] += p2
        i += 3
        if scores[1] >= 1000:
            break
    return min(scores) * (i-1)


@lru_cache(None)
def play_game(p1, p2):
    if p1[0] >= 21:
        return (1, 0)
    if p2[0] >= 21:
        return (0, 1)

    return reduce(
        lambda a, b: (a[0]+b[0], a[1]+b[1]),
        (
            play_game(
                p2,
                (
                    p1[0] + BOARD[(p1[1]+roll) % 10],
                    BOARD[(p1[1]+roll) % 10]
                )
            )
            for roll in DIRAC_SUMS
        )
    )[::-1]


def second_part(sp1, sp2):
    return max(play_game((0, sp1), (0, sp2)))


with open('2021/inputs/day21.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    p1, p2 = int(lns[0][-1]), int(lns[1][-1])
    stdout.write(f'Day 1\nFirst part: {first_part(p1,p2)}\n')
    stdout.write(f'Second part: {second_part(p1,p2)}\n')
