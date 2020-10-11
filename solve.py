
def is_valid(puzzle, x, y, val):
    ''' checks if val is valid fox x and y positions in the puzzle '''

    #  check if row allows to place val and if  col allows to place val
    for i in range(0, 9):
        if puzzle[x][i] == val\
           or puzzle[i][y] == val:
            return False

    # check box
    x_offset = x//3*3
    y_offset = y//3*3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[x_offset+i][y_offset+j] == val:
                return False
    # all criteria pass is a valid sudoku move
    return True


def solve(puzzle):
    for x in range(9):  # for all rows
        for y in range(9):  # for all cols
            if puzzle[x][y] == 0:  # if it finds an empty spot (=0)

                # tries all values
                for val in range(1, 10):

                    if is_valid(puzzle, x, y, val):
                        puzzle[x][y] = val
                        result = solve(puzzle)

                        if result is not None:  # found solution
                            return result

                        puzzle[x][y] = 0  # continue exploring

                return None  # no valid possible with this solution
    return puzzle  # solution has been found
