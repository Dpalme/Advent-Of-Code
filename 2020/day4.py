from sys import stdout


def inr(mn, mx, val):
    val = int(val)
    return mn <= val and mx >= val


def first_part(inp_str):
    psss = []
    for ln in inp_str.split("\n\n"):
        pss = {p[0]: p[1]
               for p in [pr.split(':')
                         for pr in ln.replace('\n', ' ').split()]}
        if ("byr" in pss and "iyr" in pss and
            "eyr" in pss and "hgt" in pss and
            "hcl" in pss and "ecl" in pss and
                "pid" in pss):
            psss.append(pss)
    return psss


def second_part(psss):
    return sum((inr(1920, 2002, pss["byr"]) *
                inr(2010, 2020, pss["iyr"]) *
                inr(2020, 2030, pss["eyr"]) *
                (("cm" in pss["hgt"] and
                    inr(150, 193, pss["hgt"][:-2])) or
                 ("in" in pss["hgt"] and
                    inr(59, 76, pss["hgt"][:-2]))) *
                ("#" in pss["hcl"] and len(pss["hcl"]) == 7) *
                pss["ecl"] in ("amb", "blu", "brn", "gry",
                               "grn", "hzl", "oth") and
                len(pss["pid"]) == 9) for pss in psss)


with open('2020/inputs/day4.txt', 'r') as inp:
    psss = first_part(inp.read())
    stdout.write(f'Day 4\nFirst part: {len(psss)}\n')
    stdout.write(f'Second part: {second_part(psss)}\n')
