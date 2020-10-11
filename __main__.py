import solve


def __str__puzzle(puzzle):
    s = ""
    for i in range(len(puzzle)):

        if i % 3 == 0:
            s += "_________________________________________\n"
        s += "|"

        for j in range(len(puzzle[i])):
            if j % 3 == 0:
                s += "|"
            s += " {} |".format(puzzle[i][j])
        s += "|\n"
    s += "_________________________________________\n"
    return s


if __name__ == "__main__":

    # puzzle = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    puzzle = [[4, 0, 3, 0, 0, 2, 0, 7, 0],
              [0, 8, 5, 0, 1, 0, 0, 0, 4],
              [7, 0, 0, 0, 0, 0, 0, 0, 0],
              [2, 0, 6, 0, 9, 0, 0, 0, 0],
              [0, 7, 0, 0, 0, 0, 0, 0, 6],
              [0, 0, 0, 0, 3, 0, 8, 4, 0],
              [0, 0, 0, 0, 0, 0, 4, 0, 0],
              [0, 9, 0, 0, 8, 0, 0, 3, 5],
              [0, 0, 2, 3, 0, 0, 6, 1, 0]]
    print("Puzzle to solve: ")
    print(__str__puzzle(puzzle))

    input("press enter to solve...")
    print("")
    solution = solve.solve(puzzle)

    if solution is None:
        print("No solution was found!")
    else:
        print("Solution was found!")
        print(__str__puzzle(solution))
