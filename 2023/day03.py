from sys import stdout
import functools
import re
import itertools


def first_part(lns):
    part_numbers = []

    for y, row in enumerate(lns):
        if re.search(r'\d+', row) is None:
            continue
        for numbers_match in re.finditer('\d+', row):
            if numbers_match is None:
                continue
            [x_min, x_max] = numbers_match.regs[0]
            search_string = ''.join(
                            lns[y + i][x_min - (x_min > 0):x_max + (x_max < len(row))]
                            for i in range(-1,2)
                            if 0 <= y + i <= len(lns) - 1
                            )
            if re.search(r'[^0-9.]', search_string) is not None:
                part_numbers.append(numbers_match.group(0))

    return sum(map(int, part_numbers))

class XYPlane(dict):
    def __init__(self, lns):
        super().__init__()
        for y, row in enumerate(lns):
            for x, value in enumerate(row):
                self[(x,y)] = value

    def coord(self, crd, val=None):
        if crd not in self:
            return -1
        if val is not None:
            self[crd] = val
        return self[crd]
    
    def get_matching_neighbors_coords(self, crd, conditional_func):
        x, y = crd
        for dx, dy in itertools.product((-1, 0, 1), repeat=2):
            if dx == 0 and dy == 0:
                continue
            neighbor_coord = (x+dx, y+dy)
            neighbor_value = self.coord(crd=neighbor_coord)
            if neighbor_value == -1:
                continue
            if conditional_func(neighbor_value):
                yield neighbor_coord

def traverse_coordinates(lines):
    for y, row in enumerate(lines):
        for x, value in enumerate(row):
            yield x, y, value

def second_part(lns):
    input_plane = XYPlane(lns)
    part_numbers = []
    
    for x, y, value in traverse_coordinates(lns):
        if value != '*':
            continue
        digit_neighbor_coordinates = input_plane.get_matching_neighbors_coords(
            crd=(x,y), conditional_func=lambda a: a.isdigit())
        digit_neighbor_coordinates = tuple(digit_neighbor_coordinates)
        if len(digit_neighbor_coordinates) < 2:
            continue
        number_neighbors = set()
        for coordinate in digit_neighbor_coordinates:
            nx, ny = coordinate
            line_where_the_number_is = lns[ny]
            value = line_where_the_number_is[nx]
            forward_look = line_where_the_number_is[nx + 1:]
            for item in forward_look:
                if item.isdigit():
                    value += item
                else:
                    break
            backward_look = line_where_the_number_is[:nx][::-1]
            for item in backward_look:
                if item.isdigit():
                    value = item + value
                else:
                    break
            number_neighbors.add(int(value))
        if len(number_neighbors) == 2:
            part_numbers.append(functools.reduce(lambda a,b: a*b, number_neighbors))

    return sum(part_numbers)


with open('2023/inputs/day03.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 3\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
