# A simple backtracking algorithim, adapted from "Python Sudoku Solver - Computerphile"
# https://www.youtube.com/watch?v=G_UYXzGuqvM

import check
import main

def backtrack_solve(puzzle_array):
    # Iterates over rows and columns
    for row in range(main.N):
        for col in range(main.N):

            # If space at row,col coord is "empty" aka 0, start testing legal numbers 1-9
            if puzzle_array[row][col] == 0:
                for number in range(1,10):

                    # If a number is legal, sets the space to be that legal number
                    # Then, recursively runs through solving again on puzzle
                    # If no solution possible (aka for number in range(1,10) fails), returns None...
                    # ...effectively going back one step (backtracking)
                    if check.is_legal(puzzle_array, row, col, number):
                        puzzle_array[row][col] = number

                        #If the return type is not None, returns the finished solved array
                        if backtrack_solve(puzzle_array) is not None:
                            return puzzle_array
                        puzzle_array[row][col] = 0
                return None
    
    # If iterated through all of rows and cols, returns solved array
    return puzzle_array