import math

# Define N matrix size (standard is 9x9)
N = 9

test_solution_string = "915684732837215964462973185143867529798452613526139847654728391389541276271396458"

test_puzzle_string = "910080002037200000400900180000067009000400000020100807600000091080000270000000400"

#Prints array formatted puzzle
def print_board(array):
    for row in range(N):
        for col in range(N):
            print (array[row][col], end=" ")
        print()
    print()


# Converts a puzzle formatted as string to 2d array format
def puzzle_string_to_array(puzz_string):
    full_list = [ord(char)-ord('0') for char in puzz_string]
    puzz_array = []

    for row in range(0, N*N, N):
        temp = row
        puzz_array.append(full_list[temp:temp + N])

    return puzz_array


def check_row(puzzle, row, number):
    for col in range(N):
        if puzzle[row][col] == number:
            return False
    return True



def check_col(puzzle, col, number):
    for row in range(N):
        if puzzle[row][col] == number:
            return False
    return True

def check_square(puzzle, row, col, number):
    firstRow = row - row % 3
    firstCol = col - col % 3
    for i in range(firstRow, firstRow + int(math.sqrt(N))):
        for j in range(firstCol, firstCol + int(math.sqrt(N))):
            if puzzle[i][j] == number:
                return False
    return True


def is_legal(puzzle, row, col, number):
    return check_row(puzzle, row, number) and check_col(puzzle, col, number) and check_square(puzzle, row, col, number)

def calculate_possible(puzzle, row, col):
    legal_list = []
    for number in range(N):
        if is_legal(puzzle, row, col, number):
            legal_list.append(number)
    return legal_list



print("Test puzzle (0 is empty):")
test_puzzle = puzzle_string_to_array(test_puzzle_string)
print_board(test_puzzle)

print("Test solution:")
test_solution = puzzle_string_to_array(test_solution_string)
print_board(test_solution)

print("Is 4 a legal value in test_puzzle[0][5]? (should be True based on solution)")
print(is_legal(test_puzzle, 0, 5, 4))
print()

print("Is 2 a legal value in test_puzzle[0][4]? (should be False based on solution)")
print(is_legal(test_puzzle, 0, 4, 2))
print()

print("Is 5 a legal value in square of test_puzzle[2][1]? (should be True based on solution)")
print(check_square(test_puzzle, 2, 1, 5))
print()

print("Is 9 a legal value in square of test_puzzle[2][1]? (should be False based on solution)")
print(check_square(test_puzzle, 2, 1, 9))
print()
