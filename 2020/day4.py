with open('2020/inputs/day4.txt', 'r') as inp:
    input_string = inp.read()


def in_range(min, max, value):
    return min <= value and max >= value


def first_part():
    passport = {}
    passports = []
    for line in input_string.split("\n"):
        if line != "":
            for propert in [propert.split(':') for propert in line.split()]:
                passport[propert[0]] = propert[1]
        else:
            if ("byr" in passport and "iyr" in passport and
                "eyr" in passport and "hgt" in passport and
                "hcl" in passport and "ecl" in passport and
                    "pid" in passport):
                passports.append(passport)
            passport = {}
    return passports


def second_part(passports=first_part()):
    valid = 0
    for passport in passports:
        valid += (in_range(1920, 2002, int(passport["byr"])) *
                  in_range(2010, 2020, int(passport["iyr"])) *
                  in_range(2020, 2030, int(passport["eyr"])) *
                  (("cm" in passport["hgt"] and in_range(150, 193, int(passport["hgt"][:-2]))) or
                   ("in" in passport["hgt"] and in_range(59, 76, int(passport["hgt"][:-2])))) *
                  ("#" in passport["hcl"] and len(passport["hcl"]) == 7) *
                  passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and
                  len(passport["pid"]) == 9)
    return valid


if __name__ == "__main__":
    passports = first_part()
    print("First part %d" % len(passports))
    print("Second part %d" % second_part(passports))
