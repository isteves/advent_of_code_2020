test_cases = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def check_cases(x):
    input_split = x.split("\n\n")
    input_sets = [set(i.replace("\n", "")) for i in input_split]
    input_set_lengths = map(len, input_sets)
    return list(input_set_lengths)


check_cases(test_cases)

file = open("raw/06.txt").read()
all_cases = check_cases(file)
sum(all_cases)

# Part Two


def check_intersections(x):
    input_split = x.split("\n\n")
    input_split_again = [i.split("\n") for i in input_split]
    input_sets = [list(map(set, i)) for i in input_split_again]
    group_intersections = [set.intersection(*i) for i in input_sets]
    set_lengths = map(len, group_intersections)
    return list(set_lengths)


check_intersections(test_cases)
all_intersections = check_intersections(file)
sum(all_intersections)
