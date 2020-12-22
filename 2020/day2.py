from re import search, findall
from sys import stdout


def first_part(input_data):
    valid = 0
    for line in input_data:
        rs = search(r'(\d*?)-(\d*)\s(\w):\s(.*)', line)
        valid += (int(rs.group(1)) <=
                  len(findall(rs.group(3), rs.group(4))) <=
                  int(rs.group(2)))
    return valid


def second_part(input_data):
    valid = 0
    for line in input_data:
        rs = search(r'(\d*?)-(\d*)\s(\D):\s(\D*)', line)
        pos1, pos2, letter, password = int(rs.group(1)) - 1, int(
            rs.group(2)) - 1, rs.group(3), rs.group(4)
        valid += (password[pos1] == letter) * (password[pos2] != letter) + \
            (password[pos2] == letter) * (password[pos1] != letter)
    return valid


with open('2020/inputs/day2.txt', 'r') as inp:
    inp_str = inp.readlines()
    stdout.write(f'Day 2\nFirst part: {first_part(inp_str)}\n')
    stdout.write(f'Second part: {second_part(inp_str)}\n')
