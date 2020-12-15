test_cases = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

def find_seat(x):
    row_range = list(range(0, 128))
    for i in x[:7]:
        row_range = split_halves(row_range, i)

    col_range = list(range(0, 8))
    for i in x[7:]:
        col_range = split_halves(col_range, i)

    row = row_range[0]
    col = col_range[0]
    seat_id = row * 8 + col

    return row, col, seat_id


def split_halves(seat_range, type):
    halfway_point = int(len(seat_range) / 2)
    lower_half, upper_half = seat_range[:halfway_point], seat_range[halfway_point:]
    if type in ("F", "L"):
        return lower_half
    elif type in ("B", "R"):
        return upper_half

x = "FBFBBFFRLR"
find_seat(x)
test_case_result = list(map(find_seat, test_cases))

assert test_case_result == [(70, 7, 567), (14, 7, 119), (102, 4, 820)]

file = open("raw/05.txt")
input = file.read().split("\n")

input_results = list(map(find_seat, input))
seat_ids = [i[2] for i in input_results]
max(seat_ids)

seat_ids.sort()
for i in range(0, len(seat_ids)):
    id_diff = seat_ids[i + 1] - seat_ids[i]
    if id_diff == 2:
        print(seat_ids[i + 1], seat_ids[i] )
        break
