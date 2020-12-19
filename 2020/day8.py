from sys import stdout


def evaluar(lines, br=False):
    curr, acum, ran = 0, 0, set()
    while curr < len(lines):
        if curr in ran:
            if br:
                break
            else:
                return False
        cmd, val = lines[curr][:3], int(lines[curr][3:])
        ran.add(curr)
        curr += val if cmd == "jmp" else 1
        acum += val * (cmd == 'acc')
    return acum


def first_part(inp_str):
    return evaluar([ln for ln in inp_str.split('\n')], True)


def second_part(inp_str):
    lines = [ln for ln in inp_str.split('\n')]
    change = {nbr: ln for nbr, ln in enumerate(inp_str.split('\n'))
              if ln[:3] in ['jmp', 'nop']}

    for nbr, ln in change.items():
        nlines = lines.copy()
        nlines[nbr] = ('nop' if ln[:3] == 'jmp' else 'jmp') + ln[3:]
        res = evaluar(nlines)
        if res:
            return res


with open('2020/inputs/day8.txt', 'r') as inp:
    inp_str = inp.read()
    stdout.write(f'Day 8\nFirst part: {first_part(inp_str)}\n')
    stdout.write(f'Second part: {second_part(inp_str)}\n')
