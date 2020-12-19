from re import match
from functools import lru_cache
rls = {}


@lru_cache(133)
def cmp(ind, dpth=0):
    curr = rls[ind]
    if dpth > 4:
        return ''
    if '"' in curr:
        return curr[1]
    if '|' in curr:
        frst, sec = curr.split('|')
        return '(%s)' % "|".join([''.join([cmp(i) for i in frst.split()]),
                                  ''.join([cmp(i) if i != ind else ('+'
                                          if ind == 8
                                          else '(%s)' % cmp(ind, dpth+1))
                                          for i in sec.split()])])
    return r''.join([cmp(i) for i in curr.split()])


def first_part(exps):
    return sum([match('^'+cmp('0')+'$', exp) is not None for exp in exps])


def second_part(exps):
    rls['8'], rls['11'] = '42 | 42 8', '42 31 | 42 11 31'
    return sum([match('^'+cmp('0')+'$', exp) is not None for exp in exps])


with open('2020/inputs/day19.txt', 'r') as inp:
    inp_str = inp.read().split('\n\n')
    rls, exps = {exp[:exp.find(':')]: exp[exp.find(':') + 2:]
                 for exp in inp_str[0].split('\n')}, inp_str[1].split('\n')
    print('First part: %d' % first_part(exps))
    cmp.cache_clear()
    print('Second part: %d' % second_part(exps))
