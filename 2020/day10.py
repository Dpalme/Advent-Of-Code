# region input_string
input_string = '''86
149
4
75
87
132
12
115
62
61
153
78
138
43
88
108
59
152
109
63
42
60
7
104
49
156
35
2
52
72
125
94
46
136
26
16
76
117
116
150
20
13
141
131
127
67
3
40
54
82
36
100
41
56
146
157
89
23
8
55
111
135
144
77
124
18
53
92
126
101
69
27
145
11
151
31
19
34
17
130
118
28
107
137
68
93
85
66
97
110
37
114
79
121
1'''
test = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''
test2 = '''16
10
15
5
1
11
7
19
6
12
4'''
# endregion


def first_part(input_data=input_string):
    adapts = set([int(nbr) for nbr in input_data.split('\n')])
    adds = [0, 0, 0, 1]
    for adap in adapts:
        adds[adap - adds[0]] += 1
        adds[0] = adap
    return adds[1] * adds[3]


def second_part(input_data=input_string):
    adapts = sorted([0] + [int(nbr) for nbr in input_data.split('\n')])
    acum = [1] + [0 for i in range(len(adapts) - 1)]
    for ind in range(len(adapts)):
        acum[ind] += sum([acum[ind2] for ind2, imp in enumerate(adapts[:ind])
                          if adapts[ind] - adapts[ind2] <= 3])
    return acum[-1]


if __name__ == '__main__':
    print('First part: %d' % first_part())
    print('Second part: %d' % second_part())
