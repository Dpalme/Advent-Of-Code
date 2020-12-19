from re import match
from functools import lru_cache
rules = {}


@lru_cache(None)
def get_exp(index):
    rule = rules[index]
    if '"' in rule:
        return rule[1]
    elif '|' in rule:
        frst = [get_exp(i) for i in rule[:rule.find('|')].split()]
        scnd = [get_exp(i) for i in rule[rule.find('|')+1:].split()]
        return '(%s)' % "|".join(["".join(frst if None not in frst else ''),
                                  "".join(scnd if None not in scnd else '')])
    else:
        return r''.join([get_exp(i) for i in rule.split()])


def first_part(exps):
    return sum([match('^'+get_exp('0')+'$', exp) is not None for exp in exps])


def second_part(exps):
    rules['8'], rules['11'] = '42 | 42 8', '42 31 | 42 11 31'
    return sum([match('^'+get_exp('0')+'$', exp) is not None for exp in exps])


with open('2020/inputs/day19.txt', 'r') as inp:
    inp_str = inp.read().split('\n\n')
    rules = {exp[:exp.find(':')]: exp[exp.find(':') + 2:]
             for exp in inp_str[0].split('\n')}
    print('First part: %d' % first_part(inp_str[1].split('\n')))
    print('Second part: %d' % second_part(inp_str))
