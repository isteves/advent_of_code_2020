file = open("../raw/01.txt")

input = file.read()

input_lst = input.split("\n")

# Part One

d = {}

for i in input_lst:
    inv = 2020 - int(i)
    if inv in d.keys():
        out = [int(i), inv]
        print(out)
        break
    d[int(i)] = inv
    print("Input the values", i, ":", inv)

out[0] * out[1]

# Part Two

d = {}
d2 = {}
input_lst_int = [int(i) for i in input_lst[0:len(input_lst) - 1]]
input_lst_int.sort()

for i in input_lst_int:
    for j in input_lst_int:
        inv2 = 2020 - i - j
        if inv2 in input_lst_int:
            out = [i, j, inv2]
            print(out)
            break

# not the most robust but it works

out[0] * out[1] * out[2]