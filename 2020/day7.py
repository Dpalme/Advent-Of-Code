from re import search
from sys import stdout
from functools import lru_cache

with open('2020/inputs/day7.txt', 'r') as inp:
    inp_str = inp.read().split('\n')


@lru_cache(1)
def get_regex():
    res = set()
    for line in inp_str:
        rs = search(r'(.*)\scontain\s(.*)', line[:-1])
        res.add((rs.group(1), rs.group(2)))
    return res


@lru_cache(None)
def get_directs(bag):
    direct = []
    for key, cont in get_regex():
        if bag in cont or bag[:-1] in cont:
            direct.append(key)
    return list(set(direct))


def first_part():
    direct = get_directs('shiny gold bag')
    [direct.extend(get_directs(base)) for base in direct]
    return len(set(direct))


@lru_cache(1)
def get_bags():
    bags = {}
    for key, cont in get_regex():
        bags[key] = {bag[2:]: int(bag[0]) for bag in cont.split(
            ', ')} if 'no' not in cont else 0
    return bags


@lru_cache(None)
def count_bags(key):
    if key[-1] != 's':
        key += 's'
    bags = get_bags()
    return (sum(bnum + bnum * count_bags(bag)
                for bag, bnum in bags[key].items())
            if isinstance(bags[key], dict) else 0)


def second_part(inp_str):
    return count_bags('shiny gold bags')


stdout.write(f'Day 7\nFirst part: {first_part()}\n')
stdout.write(f'Second part: {second_part(inp_str)}\n')
