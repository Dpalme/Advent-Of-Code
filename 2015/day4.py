import hashlib

input_string = 'bgvyzdsv'


def first_part(input_data=input_string):
    for i in range(2000000):
        curr_hash = hashlib.md5((input_data + str(i)).encode()).hexdigest()
        if curr_hash[:5] == "0"*5:
            return i


def second_part(input_data=input_string):
    for i in range(2000000):
        curr_hash = hashlib.md5((input_data + str(i)).encode()).hexdigest()
        if curr_hash[:6] == "0"*6:
            return i


if __name__ == '__main__':
    print('First part: %d' % first_part())
    print('Second part: %d' % second_part())
