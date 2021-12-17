from functools import reduce
from sys import stdout


def read_subpackets(p, mx=999999):
    i, res, n = 0, [], 0
    while len(p) > 6 and '1' in p and n < mx:
        v, t = int(p[:3], 2), int(p[3:6], 2)
        if t == 4:
            x, c = 6, ""
            while p[x] != '0':
                c, x = c + p[x+1:x+5], x+5
            c, x = int(c + p[x+1:x+5], 2), x + 5
        else:
            l = 11 if p[6] == '1' else 15
            pl = int(p[7:7+l], 2)
            if l == 15:
                c = read_subpackets(p[7+l:7+l+pl])
                x = 7+l+pl
            else:
                c = read_subpackets(p[7+l:], pl)
                x = 7+l+c[-1][-1]
        i,p,n = i+x,p[x:],n+1
        res.append((v, t, c, i))
    return res


def first_part(p):
    def sum_versions(c):
        v = 0
        for o in c:
            v += o[0]
            if isinstance(o[2], list):
                v += sum_versions(o[2])
        return v
    return sum_versions(read_subpackets(p))


def second_part(p):
    def process_packet(p):
        t = p[1]
        if t == 0:
            return sum(map(process_packet, p[2]))
        if t == 1:
            return reduce(lambda a,b:a*b, map(process_packet, p[2]))
        if t == 2:
            return min(map(process_packet, p[2]))
        if t == 3:
            return max(map(process_packet, p[2]))
        if t == 4:
            return p[2]
        if t == 5:
            return int(reduce(lambda a,b:a>b, map(process_packet, p[2])))
        if t == 6:
            return int(reduce(lambda a,b:a<b, map(process_packet, p[2])))
        if t == 7:
            return int(reduce(lambda a,b:a==b, map(process_packet, p[2])))
    return process_packet(read_subpackets(p)[0])


with open('2021/inputs/day16.txt', 'r') as inp:
    ln = ''.join(map(lambda a: str(bin(int(a, 16))[2:]).zfill(4), inp.readline().strip()))
    stdout.write(f'Day 16\nFirst part: {first_part(ln)}\n')
    stdout.write(f'Second part: {second_part(ln)}\n')
