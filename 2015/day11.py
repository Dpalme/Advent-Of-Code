inp_str = 'vzbxkghb'


def check_valid(nmbrs):
    letters = (8 not in nmbrs) * (14 not in nmbrs) * (11 not in nmbrs)
    straight, pair, bind = 1, 0, 8
    for i, num in enumerate(nmbrs[:-1]):
        n1 = nmbrs[i+1]
        if i != 6:
            straight *= 1 - ((num+1 == n1) * (num+2 == nmbrs[i+2]))
        if i != bind:
            if num == n1:
                bind, pair = i+1, pair+1
    return letters * (not straight) * (pair >= 2)


def nxt_password(psswrd):
    nmbrs = [(ord(char) - 97) for char in psswrd]
    nmbrs[7] += 1
    while not check_valid(nmbrs):
        nmbrs[7] += 1
        if nmbrs[7] > 25:
            for i, num in enumerate(reversed(nmbrs)):
                if num > 25:
                    nmbrs[7-i], nmbrs[6-i] = 0, nmbrs[6-i]+1
    return "".join([chr(num + 97) for num in nmbrs])


if __name__ == '__main__':
    f_password = nxt_password(inp_str)
    print(f'First part: {f_password}')
    print(f'Second part: {nxt_password(f_password)}')
