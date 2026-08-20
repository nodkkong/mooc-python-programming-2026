# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            block.append(sudoku[r][c])
    for number in range(1, 10):
        if block.count(number) > 1:
            return False
    return True