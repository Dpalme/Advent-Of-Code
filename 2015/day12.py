from sys import stdout as std
from json import loads


def get_ints(obj, red=False):
    vals, acum = obj if isinstance(obj, list) else obj.values(), 0
    for val in vals:
        if red and isinstance(obj, dict):
            if 'red' in vals or 'red' in obj.keys():
                return 0
        if isinstance(val, int):
            acum += val
        elif isinstance(val, (dict, list)):
            acum += get_ints(val, red)
    return acum


def first_part(json_obj):
    return get_ints(json_obj)


def second_part(json_obj):
    return get_ints(json_obj, True)


with open('2015/inputs/day12.txt', 'r') as inp:
    json_obj = loads(inp.read())
    std.write(f'Day 12\nFirst part: {first_part(json_obj)}\n')
    std.write(f'Second part: {second_part(json_obj)}\n')
