from sys import stdout


def inr(mn, mx, val):
    return mn <= val and mx >= val


def first_part(inp_str):
    pss = {}
    psss = []
    for line in inp_str.split("\n"):
        if line != "":
            for propert in [propert.split(':') for propert in line.split()]:
                pss[propert[0]] = propert[1]
        else:
            if ("byr" in pss and "iyr" in pss and
                "eyr" in pss and "hgt" in pss and
                "hcl" in pss and "ecl" in pss and
                    "pid" in pss):
                psss.append(pss)
            pss = {}
    return psss


def second_part(psss):
    valid = 0
    for pss in psss:
        valid += (inr(1920, 2002, int(pss["byr"])) *
                  inr(2010, 2020, int(pss["iyr"])) *
                  inr(2020, 2030, int(pss["eyr"])) *
                  (("cm" in pss["hgt"] and
                    inr(150, 193, int(pss["hgt"][:-2]))) or
                   ("in" in pss["hgt"] and
                    inr(59, 76, int(pss["hgt"][:-2])))) *
                  ("#" in pss["hcl"] and len(pss["hcl"]) == 7) *
                  pss["ecl"] in ["amb", "blu", "brn", "gry",
                                 "grn", "hzl", "oth"] and
                  len(pss["pid"]) == 9)
    return valid


with open('2020/inputs/day4.txt', 'r') as inp:
    psss = first_part(inp.read())
    stdout.write(f'Day 4\nFirst part: {len(psss)}\n')
    stdout.write(f'Second part: {second_part(psss)}\n')
