# write your solution here
def read_matrix():
    with open("matrix.txt") as f:
        rows = []
        for line in f:
            row = []
            for num in line.replace("\n", "").split(","):
                row.append(int(num))
            rows.append(row)
    return rows


def matrix_sum():
    rows = read_matrix()
    total = 0
    for row in rows:
        for num in row:
            total += num
    return total


def matrix_max():
    rows = read_matrix()
    max_num = None
    for row in rows:
        for num in row:
            if max_num is None or num > max_num:
                max_num = num
    return max_num

def row_sums():
    rows = read_matrix()
    row_total = []
    for row in rows:
        row_total.append(sum(row))
    return row_total