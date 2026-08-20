# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for number in range(1, 10):
        if row.count(number) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no])
    
    for number in range(1, 10):
        if column.count(number) > 1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            block.append(sudoku[r][c])
    for number in range(1, 10):
        if block.count(number) > 1:
            return False
    return True


def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False

    for r in range(0, 7, 3):
        for c in range(0, 7, 3):
            if not block_correct(sudoku, r, c):
                return False

    return True