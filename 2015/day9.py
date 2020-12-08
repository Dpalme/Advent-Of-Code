import re
import itertools

# region input_string
input_string = '''Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46'''
# endregion


def get_routes(input_data=input_string):
    locs, rt = [], {}
    for line in input_data.split('\n'):
        res = re.search(r'(.*)\sto\s(.*)\s=\s(\d*)', line)
        ct1, ct2, dst = res.group(1), res.group(2), int(res.group(3))
        rt[ct1+ct2], rt[ct2+ct1] = dst, dst
        locs.extend([ct for ct in [ct1, ct2] if ct not in locs])
    return locs, rt


def first_part(input_data=input_string):
    (locs, rt), min_dist = get_routes(input_data), 9999
    for itt in itertools.permutations(locs, len(locs)):
        c1, c2, c3, c4, c5, c6, c7, c8 = itt
        dist = rt[c1+c2] + rt[c2+c3] + rt[c3+c4] + \
            rt[c4+c5] + rt[c5+c6] + rt[c6+c7] + rt[c7+c8]
        min_dist = dist if dist < min_dist else min_dist
    return min_dist


def second_part(input_data=input_string):
    (locs, rt), max_dis = get_routes(input_data), 0
    for itt in itertools.permutations(locs, len(locs)):
        c1, c2, c3, c4, c5, c6, c7, c8 = itt
        dist = rt[c1+c2] + rt[c2+c3] + rt[c3+c4] + \
            rt[c4+c5] + rt[c5+c6] + rt[c6+c7] + rt[c7+c8]
        max_dis = dist if dist > max_dis else max_dis
    return max_dis


if __name__ == '__main__':
    print('First part: %d' % first_part())
    print('Second part: %d' % second_part())
