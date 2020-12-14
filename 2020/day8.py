def first_part(input_data):
    curr, acum, ran = 0, 0, []
    lines = [line for line in input_data.split('\n')]
    while curr < len(lines) and curr not in ran:
        cmd, var = lines[curr].split()
        ran.append(curr)
        if cmd == "jmp":
            curr += int(var)
        else:
            acum += int(var) if cmd == 'acc' else 0
            curr += 1
    return acum


def evaluar(lines):
    curr, acum, ran = 0, 0, []
    while curr < len(lines):
        if curr in ran:
            return False
        cmd, var = lines[curr].split()
        ran.append(curr)
        if cmd == "jmp":
            curr += int(var)
        else:
            acum += int(var) if cmd == 'acc' else 0
            curr += 1
    return acum


def second_part(input_data):
    lines, change = [line for line in input_data.split('\n')], {}
    change = {nbr: line[:3] for nbr, line in enumerate(
        input_data.split('\n')) if 'jmp' in line or 'nop' in line}

    for nbr, ins in change.items():
        nlines = lines.copy()
        nlines[nbr] = ('nop' if ins == 'jmp' else 'jmp') + nlines[nbr][3:]
        res = evaluar(nlines)
        if res:
            return res
    return 0


if __name__ == '__main__':
    with open('2020/inputs/day8.txt', 'r') as inp:
        input_string = inp.read()
        print('First part: %d' % first_part(input_string))
        print('Second part: %d' % second_part(input_string))
