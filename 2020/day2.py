import re


def first_part(input_data):
    valid = 0
    for line in input_data.split("\n"):
        res = re.search(r'(\d*?)-(\d*)\s(\w):\s(.*)', line)
        low, upp = int(res.group(1)), int(res.group(2))
        value = len(re.findall(res.group(3), res.group(4)))
        valid += (low <= value) and (value <= upp)
    return valid


def second_part(input_data):
    valid = 0
    for line in input_data.split("\n"):
        res = re.search(r'(\d*?)-(\d*)\s(\D):\s(\D*)', line)
        pos1, pos2, letter, password = int(res.group(1)) - 1, int(
            res.group(2)) - 1, res.group(3), res.group(4)
        valid += (password[pos1] == letter) * (password[pos2] != letter) + \
            (password[pos2] == letter) * (password[pos1] != letter)
    return valid


if __name__ == "__main__":
    with open('2020/inputs/day2.txt', 'r') as inp:
        inp_str = inp.read()
        print('First part: %d' % first_part(inp_str))
        print('Second part: %d' % second_part(inp_str))
