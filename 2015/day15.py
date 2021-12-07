from functools import reduce
from sys import stdout as std


def first_part(ingredients):
    for i in range(100):
        ings = ()
        for 
        ings = ingredients[0]
        capacity = reduce(lambda a, b: a+b, ingredients[0][0])
    return max(reduce(lambda a, b: a*b, (sum(x) * (sum(x) > 0)
               for x in zip(*ingredients.values()))) for comb in)


def second_part(ingredients):
    return -1


with open('2015/inputs/test.txt', 'r') as inp:
    ingredients = []
    for i in inp.read().split('\n'):
        i = i.split()
        ingredients.append(int(i[2][:-1]), int(i[4][:-1]),
                        int(i[6][:-1]), int(i[6][:-1]), int(i[-1]))
    std.write('Day 25\nFirst part: ')
    std.write(f'{first_part(ingredients)}\n')
    std.write('Second part: ')
    std.write(f'{second_part(ingredients)}\n')
