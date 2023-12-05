from sys import stdout

import re
import functools

def round_exceeds(game: str, color: str, max_value: int) -> bool:
    return any(map(lambda a: a > max_value,
                map(int, re.findall(f'(\d+) {color}', game))))


def game_is_not_possible(game: str,
                        max_green: int,
                        max_red: int,
                        max_blue: int) -> bool:
    return any(map(lambda a: round_exceeds(*a), [(game, 'green', max_green),
                                    (game, 'blue', max_blue),
                                    (game, 'red', max_red)]))


def first_part(lns):
    return sum(index + 1
               for index, game in enumerate(lns)
               if not game_is_not_possible(game=game,
                                   max_blue=14,
                                   max_green=13,
                                   max_red=12))


def second_part(lns):
    COLORS = ('red', 'green', 'blue')
    # sum all games
    return sum(
        # multiply the three values together
        map(
            functools.partial(
                functools.reduce,
                lambda a,b: a*b,
            ),
            # find the max cubes for each color on each round
            map(
                lambda game: (
                    max(map(int, re.findall(f'(\d+) {color}', game)))
                    for color in COLORS
                ),
                lns
            )
        )
    )


with open('2023/inputs/day02.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 2\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
