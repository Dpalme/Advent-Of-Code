from re import match
from functools import lru_cache
rules = {}


@lru_cache(132)
def get_exp(ind):
    rule = rules[ind]
    if '"' in rule:
        return rule[1]
    elif '|' in rule:
        ind2 = rule.find('|')
        frst = [get_exp(i) for i in rule[:ind2].split()]
        scnd = [get_exp(i) if i != ind else ('+'
                if ind == 8 else '(?:' + "|".join([f'{get_exp("42")}{{{i}}}{get_exp("31")}{{{i}}}' for i in range(1, 5)]) + ')')
                for i in rule[ind2+1:].split()]
        return '(%s)' % "|".join(["".join(frst if None not in frst else ''),
                                  "".join(scnd if None not in scnd else '')])
    else:
        return r''.join([get_exp(i) for i in rule.split()])


def first_part(exps):  # 111
    return sum([match('^'+get_exp('0')+'$', exp) is not None for exp in exps])


def second_part(exps):  # 343
    rules['8'], rules['11'] = '42 | 42 8', '42 31 | 11'
    return sum([match('^'+get_exp('0')+'$', exp) is not None for exp in exps])


with open('2020/inputs/day19.txt', 'r') as inp:
    inp_str = inp.read().split('\n\n')
    rules, exps = {exp[:exp.find(':')]: exp[exp.find(':') + 2:]
                   for exp in inp_str[0].split('\n')}, inp_str[1].split('\n')
    print('First part: %d' % first_part(exps))
    get_exp.cache_clear()
    print('Second part: %d' % second_part(exps))
