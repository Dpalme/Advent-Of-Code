from functools import reduce
from sys import stdout
from re import sub, findall


def first_part(lns):
    score = 0
    scrs = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for ln in lns:
        while len(findall(r'\(\)|\{\}|\[\]|<>', ln)):
            ln = sub(r'\(\)|\{\}|\[\]|<>', '', ln)
        ln = sub(r'\(|\{|\[|<', '', ln)
        if ln and ln[0] in scrs:
            score += scrs[ln[0]]
    return score


def second_part(ns):
    scores = []
    scrs = {'(': 1, '[': 2, '{': 3, '<': 4}
    for ln in lns:
        while len(findall(r'\(\)|\{\}|\[\]|<>', ln)):
            ln = sub(r'\(\)|\{\}|\[\]|<>', '', ln)
        oln = len(findall(r'\)|\}|\]|>', ln))
        if not oln:
            scores.append(reduce(lambda a,b: a*5 + b, (scrs[c] for c in reversed(ln))))
    return sorted(scores)[(len(scores) // 2)]


with open('2021/inputs/day10.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 10\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
