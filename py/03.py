file = open("raw/03.txt")

input = file.read()
input_lst = input.split("\n")
input_lst

## Part One

rows = len(input_lst)
cols = len(input_lst[0])
pos = list(range(0, rows - 1))
pos = [i * 3 % cols for i in pos]

input_zipped = list(zip(input_lst, pos))
input_zipped[1][1]
sum([i[0][i[1]] == "#" for i in input_zipped])

## Part Two

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.


def count_trees(input_map, right, down):
    rows = len(input_map)
    cols = len(input_map[0])
    row_range = list(range(0, rows - 1))
    pos_row = [i % down == 0 for i in row_range]
    filtered_input_map = [i[0] for i in list(zip(input_map, pos_row)) if i[1]]

    row_range_filtered = list(range(0, len(filtered_input_map)))
    pos = [i * right % cols for i in row_range_filtered]

    input_zipped = list(zip(filtered_input_map, pos))
    return sum([i[0][i[1]] == "#" for i in input_zipped])

count_trees(input_lst, 1, 2)

count_trees(input_lst, 1, 1) * count_trees(input_lst, 3, 1) * count_trees(input_lst, 5, 1) * count_trees(input_lst, 7, 1) * count_trees(input_lst, 1, 2)
