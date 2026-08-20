# Write your solution here
def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no])
    
    for number in range(1, 10):
        if column.count(number) > 1:
            return False
    return True