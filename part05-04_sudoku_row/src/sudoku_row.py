# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for number in range(1, 10):
        if row.count(number) > 1:
            return False
    return True