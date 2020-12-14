from math import cos, sin, pi


class Vector2(object):
    def __init__(self, x, y):
        self.x, self.y = int(x), int(y)

    def __add__(self, v2):
        return Vector2(self.x + v2.x, self.y + v2.y)

    def __mul__(self, val):
        return Vector2(int(self.x * val), int(self.y * val))

    @property
    def manh(self):
        return int(abs(self.x) + abs(self.y))


def first_part(input_data):
    boat, bdeg = Vector2(0, 0), 180
    dirs = {'N': Vector2(0, 1), 'W': Vector2(1, 0),
            'S': Vector2(0, -1), 'E': Vector2(-1, 0)}
    angs = {'L': -1, 'R': 1}
    for line in input_data.split('\n'):
        cmd, val = line[0], int(line[1:])
        if cmd in dirs:
            boat += dirs[cmd] * val
        elif cmd in angs:
            bdeg += angs[cmd] * val
        else:
            boat += Vector2(cos(bdeg * pi / 180), sin(bdeg * pi / 180)) * val
    return boat.manh


def second_part(input_data):
    wayp, boat = Vector2(-10, 1), Vector2(0, 0)
    dirs = {'N': Vector2(0, 1), 'W': Vector2(1, 0),
            'S': Vector2(0, -1), 'E': Vector2(-1, 0)}
    for line in input_data.split('\n'):
        cmd, val = line[0], int(line[1:])
        if cmd in dirs:
            wayp += dirs[cmd] * val
        elif cmd in ['L', 'R']:
            if cmd == 'R':
                for i in range(val//90):
                    wayp.x, wayp.y = -wayp.y, wayp.x
            else:
                for i in range(val//90):
                    wayp.x, wayp.y = wayp.y, -wayp.x
        else:
            boat += wayp * val
    return boat.manh


if __name__ == '__main__':
    with open('2020/inputs/day12.txt', 'r') as inp:
        input_string = inp.read()
        print('First part: %d' % first_part(input_string))
        print('Second part: %d' % second_part(input_string))
