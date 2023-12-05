from sys import stdout
import re


def first_part(lns):
    digits = []
    for ln in lns:
        line_digits = re.findall(r'\d', ln)
        digits.append(int(line_digits[0] + line_digits[-1]))
    return sum(digits)


def second_part(lns):
    NUMBERS = {'one': 'o1e', 'two': 't2o', 'three': 't3e',
               'four': 'f4r', 'five': 'f5e', 'six': 's6x',
               'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

    def text_to_digit(ln):
        for k, v in NUMBERS.items():
            ln = re.sub(k, v, ln)
        return ln
    replaced_lns = tuple(map(text_to_digit, lns))
    return first_part(lns=replaced_lns)


with open('2023/inputs/day01.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 1\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
