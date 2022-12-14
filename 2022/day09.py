from sys import stdout


DIRECTIONS = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}


class Knot:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    @property
    def position(self) -> tuple[int, int]:
        return (self.x, self.y)

    def follow(self, other):
        if abs(other.x - self.x) >= 2:
            self.x += (other.x - self.x) >> 1
            self.y += (other.y - self.y)
        if abs(other.y - self.y) >= 2:
            self.y += (other.y - self.y) >> 1
            self.x += (other.x - self.x)


def print_visited(visited: set[tuple[int, int]]):
    for y in range(-10, 20)[::-1]:
        for x in range(-30, 30):
            if (x, y) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def print_rope(rope: list[Knot]):
    for y in range(-2, 5)[::-1]:
        for x in range(-15, 15):
            for i, knot in enumerate(rope):
                if knot.x == x and knot.y == y:
                    print('H' if i == 0 else i, end='')
                    break
            else:
                if x == 0 and y == 0:
                    print('s', end='')
                print('.', end='')
                    
        print()
    print()


def both_parts(instructions, number_of_knots: int):
    visited = set()
    rope = [Knot() for _ in range(number_of_knots)]
    for direction, distance in instructions:
        for _ in range(distance):
            dx, dy = DIRECTIONS[direction]
            rope[0].x += dx
            rope[0].y += dy
            for knot_1, knot_2 in zip(rope, rope[1:]):
                knot_2.follow(knot_1)
            print_rope(rope)
            visited.add(rope[-1].position)
    return len(visited)


with open('2022/inputs/test.txt', 'r') as inp:
    instructions = (
        *map(lambda a: (a.split()[0], int(a.split()[1])), inp.read().rsplit('\n')),)
    stdout.write(f'Day 9\nFirst part: {both_parts(instructions, 2)}\n')
    stdout.write(f'Second part: {both_parts(instructions, 10)}\n')
