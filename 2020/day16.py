from re import search


def first_part(inp_str):
    secs, error_rate = [line for line in inp_str.split('\n\n')], 0
    classes, nrby_tckts = secs[0].split('\n'), secs[2].split('\n')[1:]
    available = []
    for line in classes:
        res = search(r'.*[:]\s(\d*)-(\d*)\sor\s(\d*)-(\d*)', line)
        available.extend([str(x) for x in range(
            int(res.group(1)), int(res.group(2)) + 1)])
        available.extend([str(x) for x in range(
            int(res.group(3)), int(res.group(4)) + 1)])
    for ticket in nrby_tckts:
        for data in ticket.split(','):
            error_rate += int(data) if data not in available else 0
    return error_rate


def delete_invalid_tickets(tickets, available):
    for ticket in tickets.copy():
        for data in ticket.split(','):
            if data not in available:
                tickets.remove(ticket)
    return tickets


def second_part(inp_str):
    # Initialize variables
    secs, accum = [ln for ln in inp_str.split('\n\n')], 1
    lns = secs[0].split('\n')

    # Create classes with their range and a pool of all aceptable numbers
    classes, available = {}, []
    for line in lns:
        res = search(r'(.*)[:]\s(\d*)-(\d*)\sor\s(\d*)-(\d*)', line)
        c_range = [str(x)
                   for x in range(int(res.group(2)), int(res.group(3)) + 1)]
        c_range.extend([str(x) for x in range(
            int(res.group(4)), int(res.group(5)) + 1)])
        classes[res.group(1)] = c_range
        available.extend(c_range)

    # delete tickets with unacceptable numbers
    nrby_tckts = delete_invalid_tickets(secs[2].split('\n')[1:], available)

    # split ticket numbers into their positions
    clss_rng = {i: [] for i in range(len(classes))}
    for ticket in nrby_tckts:
        for ind, val in enumerate(ticket.split(',')):
            clss_rng[ind].append(val)

    # create a list of all possible classes for each number group
    for t_class, values in clss_rng.items():
        poss_classes = list(classes.keys())
        for poss_class in poss_classes.copy():
            curr_range = classes[poss_class]
            for value in values:
                if value not in curr_range:
                    poss_classes.remove(poss_class)
                    break
        clss_rng[t_class] = poss_classes

    # remove duplicates from possible classes
    available = list(classes.keys())
    for clas, posses in sorted(clss_rng.items(), key=lambda x: len(x[1])):
        for poss in posses.copy():
            if poss in available:
                available.remove(poss)
            else:
                clss_rng[clas].remove(poss)

    # get values from own ticket
    my_ticket = {clss_rng[i][0]: int(n) for i, n in enumerate(
        secs[1].split('\n')[1].split(','))}
    for name, value in my_ticket.items():
        if 'departure' in name:
            accum *= value
    return accum


if __name__ == '__main__':
    with open('2020/inputs/day16.txt', 'r') as inp:
        inp_str = inp.read()
        print('First part: %d' % first_part(inp_str))
        print('Second part: %d' % second_part(inp_str))
