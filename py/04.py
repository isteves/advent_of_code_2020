import re

test_case = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# valid, invalid, valid, invalid
# missing cid is fine

# first checked code below on test_case then replaced with actual_case

input = open("raw/04.txt")
actual_case = input.read()

# Part One

def extract_field(field_string):
    return field_string.split(":")[0]

def check_required_fields(fields, required_fields = required_fields):
    return all(item in fields for item in required_fields)

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = actual_case.split("\n\n")
passports_split = [re.split(" |\n", passport) for passport in passports]

passport_fields = [list(map(extract_field, field_strings)) for field_strings in passports_split]
sum(map(check_required_fields, passport_fields))

# Part Two

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

test_case_invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""
# expect 0

test_case_valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
# expect 4


def extract_field(field_string):
    field_name, field_value = field_string.split(":")
    return field_name, field_value


def check_required_fields(fields_tuple_list, required_fields = required_fields):
    fields = [i[0] for i in fields_tuple_list]
    return all(item in fields for item in required_fields)


def parse_passports(input_string):
    passports = input_string.split("\n\n")
    passports_split = [re.split(" |\n", passport) for passport in passports]
    out = [list(map(extract_field, field_strings)) for field_strings in passports_split]
    return out


def is_convertible_to_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def check_field_value(x):
    field_name, field_value = x
    if field_name == "byr":
        return 1920 <= int(field_value) <= 2002
    elif field_name == "iyr":
        return 2010 <= int(field_value) <= 2020
    elif field_name == "eyr":
        return 2020 <= int(field_value) <= 2030
    elif field_name == "hgt":
        hgt, units = field_value[:-2], field_value[-2:]
        if is_convertible_to_int(hgt):
            hgt = int(hgt)
        else:
            return False

        if units == "cm":
            return 150 <= hgt <= 193
        elif units == "in":
            return 59 <= hgt <= 76
        else:
            return False
    elif field_name == "hcl":
        hsh, color_string = field_value[0], field_value[1:7]
        if hsh != "#" or len(color_string) != 6:
            return False
        else:
            return bool(re.match('^[0-9a-f]*$', color_string))
    elif field_name == "ecl":
        return field_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field_name == "pid":
        return bool(re.match('^[0-9]*$', field_value)) and len(field_value) == 9
    elif field_name == "cid":
        return True


def check_passport_values(parsed_passport):
    if not check_required_fields(parsed_passport):
        return False

    field_values_bool = list(map(check_field_value, parsed_passport))
    return all(field_values_bool)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


passport_parsed = parse_passports(test_case_invalid)
sum(list(map(check_passport_values, passport_parsed)))

passport_parsed = parse_passports(test_case_valid)
sum(list(map(check_passport_values, passport_parsed)))

passport_parsed = parse_passports(actual_case)
sum(list(map(check_passport_values, passport_parsed)))
