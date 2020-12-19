from sys import stdout


def first_part(inp_str):
    return sum([len(set([lttr for lttr in form.replace('\n', '')]))
               for form in inp_str.split('\n\n')])


def second_part(inp_str, total=[]):
    for forms in inp_str.split('\n\n'):
        total.append([set(form) for form in forms.split('\n')])
        [total[-1][0].intersection_update(form) for form in total[-1][1:]]
    return sum([len(form[0]) for form in total])


with open('2020/inputs/day6.txt', 'r') as inp:
    inp_str = inp.read()
    stdout.write(f'Day 6\nFirst part: {first_part(inp_str)}\n')
    stdout.write(f'Second part: {second_part(inp_str)}\n')
