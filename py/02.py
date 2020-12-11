import re

file = open("../raw/02.txt")

input = file.read()

input_lst = input.split("\n")

all_inputs_split = [re.split('[ :-]', i) for i in input_lst]

# Part One

pwd_check = [int(i[0]) <=  i[4].count(i[2]) <= int(i[1]) for i in all_inputs_split if len(i) == 5]

sum(pwd_check)

# Part Two

test_cases = [
    ["1", "3", "a", "", "abcde"],
    ["1", "3", "b", "", "cdefg"],
    ["2", "9", "c", "", "ccccccccc"]
]

def apply_rule(x):
    pos1 = int(x[0])
    pos2 = int(x[1])
    ltr = x[2]
    pwd = x[4]

    check_one = pwd[pos1 - 1] == ltr
    if pos2 <= len(pwd):
        check_two = pwd[pos2 - 1] == ltr
    else:
        check_two = False

    #print(check_one, check_two)
    return check_one + check_two == 1

[apply_rule(i) for i in test_cases if len(i) == 5]

sum([apply_rule(i) for i in all_inputs_split if len(i) == 5])
