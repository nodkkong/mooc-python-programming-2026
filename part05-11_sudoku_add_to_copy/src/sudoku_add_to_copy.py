# Write your solution here
def print_sudoku(sudoku: list):
    for row_index in range(len(sudoku)):
        row = sudoku[row_index]
        for i in range(len(row)):
            if row[i] == 0:
                print("_", end=" ")
            else:
                print(row[i], end=" ")
            if i % 3 == 2 and i < 8:
                print("", end=" ")
        print()
        if row_index % 3 == 2 and row_index < 8:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list = []
    for row in sudoku:
        new_list.append(row[:])
    new_list[row_no][column_no] = number
    return new_list