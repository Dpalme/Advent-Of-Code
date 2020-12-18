from re import search

with open('2020/inputs/day7.txt', 'r') as inp:
    input_string = inp.read()


def get_directs(bag, input_data=input_string):
    direct = []
    for line in input_data.split('\n'):
        res = search(r'(.*)\scontain\s(.*)', line[:-1])
        if bag in res.group(2) or bag[:-1] in res.group(2):
            direct.append(res.group(1))
    return list(set(direct))


def first_part(input_data=input_string):
    direct = get_directs('shiny gold bag')
    for base in direct:
        direct.extend(get_directs(base))
    return len(set(direct))


def count_bags(key, bags):
    key += "s" if key[-1] != 's' else ""
    smt = sum([bnum + bnum * count_bags(bag, bags)
               for bag, bnum in bags[key].items()]) if type(bags[key]) == dict else 0
    return smt


def second_part(input_data=input_string):
    bags = {}
    for line in input_data.split('\n'):
        res = search(r'(.*)\scontain\s(.*)', line[:-1])
        bags[res.group(1)] = {bag[2:]: int(bag[0]) for bag in res.group(
            2).split(', ')} if 'no' not in res.group(2) else 0
    return count_bags('shiny gold bags', bags)


if __name__ == '__main__':
    # print('First part: %d' % first_part())
    print('Second part: %d' % second_part())
