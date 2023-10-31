import main
import math

#Checks if number is legal within a certain x coord column 
def check_row(puzzle, row, number):
    for col in range(main.N):
        if puzzle[row][col] == number:
            return False
    return True

#Checks if number is legal within a certain y coord column 
def check_col(puzzle, col, number):
    for row in range(main.N):
        if puzzle[row][col] == number:
            return False
    return True

#Checks if number is legal in the square of spaces containing an x,y coord in 2d puzzle array 
#Scales with matrix size? TBD
def check_square(puzzle, row, col, number):
    first_row = row - row % 3
    first_col = col - col % 3
    for i in range(first_row, first_row + int(math.sqrt(main.N))):
        for j in range(first_col, first_col + int(math.sqrt(main.N))):
            if puzzle[i][j] == number:
                return False
    return True


#Returns bool determining if a particular number is legal in a particular x,y coord in a 2d puzzle array
def is_legal(puzzle, row, col, number):
    return check_row(puzzle, row, number) and check_col(puzzle, col, number) and check_square(puzzle, row, col, number)