from re import match
from functools import lru_cache
rules = {}


@lru_cache(133)
def comp(ind, dpth=0):
    rule = rules[ind]
    if dpth > 4:
        return ''
    if '"' in rule:
        return rule[1]
    if '|' in rule:
        frst, sec = rule.split('|')
        return '(%s)' % "|".join([''.join([comp(i) for i in frst.split()]),
                                  ''.join([comp(i) if i != ind else ('+'
                                          if ind == 8
                                          else '(%s)' % comp(ind, dpth+1))
                                          for i in sec.split()])])
    return r''.join([comp(i) for i in rule.split()])


def first_part(exps):
    return sum([match('^'+comp('0')+'$', exp) is not None for exp in exps])


def second_part(exps):
    rules['8'], rules['11'] = '42 | 42 8', '42 31 | 42 11 31'
    return sum([match('^'+comp('0')+'$', exp) is not None for exp in exps])


with open('2020/inputs/day19.txt', 'r') as inp:
    inp_str = inp.read().split('\n\n')
    rules, exps = {exp[:exp.find(':')]: exp[exp.find(':') + 2:]
                   for exp in inp_str[0].split('\n')}, inp_str[1].split('\n')
    print('First part: %d' % first_part(exps))
    comp.cache_clear()
    print('Second part: %d' % second_part(exps))
