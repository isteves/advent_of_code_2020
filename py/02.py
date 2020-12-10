importre

file = open("../raw/02.txt")

input = file.read()

input_lst = input.split("\n")

all_inputs_split = [re.split('[ :-]', i) for i in input_lst]

pwd_check = [int(i[0]) <=  i[4].count(i[2]) <= int(i[1]) for i in all_inputs_split if len(i) == 5]

sum(pwd_check)
