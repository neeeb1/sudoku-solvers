import math

# Define N matrix size (standard is 9x9)
N = 9

# A completed test puzzle
test_solution_string = "425971368173628594869543172241795836736182945958436721597864213384217659612359487"

# Same puzzle as solution, but missing entries.
test_puzzle_string = "405001068073628500009003070240790030006102005950000021507064213080217050612300007"


# Prints array formatted puzzle
def print_board(array):
    for row in range(N):
        for col in range(N):
            print(array[row][col], end=" ")
        print()
    print()


# Converts a puzzle formatted as string to 2d array format
def puzzle_string_to_array(puzzle_string):
    full_list = [ord(char) - ord('0') for char in puzzle_string]
    puzzle_array = []

    for row in range(0, N * N, N):
        temp = row
        puzzle_array.append(full_list[temp:temp + N])

    return puzzle_array


# Checks to see if provided row
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
    first_row = row - row % 3
    first_col = col - col % 3
    for i in range(first_row, first_row + int(math.sqrt(N))):
        for j in range(first_col, first_col + int(math.sqrt(N))):
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


# Debug suite for printing puzzle, testing row, column, and square validity checkers
#
print("Test puzzle (0 is empty):")
test_puzzle = puzzle_string_to_array(test_puzzle_string)
print_board(test_puzzle)

print("Test solution:")
test_solution = puzzle_string_to_array(test_solution_string)
print_board(test_solution)
#
# print("Is 4 a legal value in test_puzzle[0][5]? (should be True based on solution)")
# print(is_legal(test_puzzle, 0, 5, 4))
# print()
#
# print("Is 2 a legal value in test_puzzle[0][4]? (should be False based on solution)")
# print(is_legal(test_puzzle, 0, 4, 2))
# print()
#
# print("Is 5 a legal value in square of test_puzzle[2][1]? (should be True )")
# print(check_square(test_puzzle, 2, 1, 5))
# print()
#
# print("Is 9 a legal value in square of test_puzzle[2][1]? (should be False based on solution)")
# print(check_square(test_puzzle, 2, 1, 9))
# print()


def backtrack_solve(puzz_string, debug = False):
    puzz_grid = puzzle_string_to_array(puzz_string)
    test_grid = puzzle_string_to_array(puzz_string)

    solved = False

    row = 0
    col = 0

    while not solved:
        backtrack = False

        while row < N:
            while col < N:
                if debug: print('row: ' + str(row) + ', col: ' + str(col) + ', test_grid value: ' + str(test_grid[row][col]))
                temp_value = test_grid[row][col]

                if backtrack:
                    tmp = puzz_grid[row][col]
                    test_grid[row][col] = tmp
                    if debug: print('set value back to puzz_grid value')

                if puzz_grid[row][col] == 0 or backtrack:
                    guess = temp_value+1
                    if debug: print('initial guess: '+str(guess))

                    if guess > N:
                        col -= 1
                        if debug: print('move back (A)')
                        backtrack = True
                        if col < 0:
                            col = N - 1
                            row -= 1

                    while guess < N+1:
                        if debug: print('guess: '+str(guess))

                        if is_legal(test_grid, row, col, guess):
                            test_grid[row][col] = guess
                            if debug: print('placed value of '+str(guess))
                            backtrack = False

                            col += 1
                            if debug: print('move forward (A)')
                            if col >= N:
                                col = 0
                                row += 1
                                if row >= N:
                                    return test_grid
                            break

                        elif guess >= N:
                            col -= 1
                            if debug: print('move back (A)')
                            backtrack = True
                            if col < 0:
                                col = N-1
                                row -= 1

                        guess += 1

                else:
                    col += 1
                    if debug: print('move forward (B)')
                    if col >= N:
                        col = 0
                        row += 1
                        if row >= N:
                            return test_grid

    return test_grid


print('starting solver')
test_board = puzzle_string_to_array(test_puzzle_string)
solution_board = puzzle_string_to_array(test_solution_string)
solved_board = backtrack_solve(test_puzzle_string)
print()
print('\"Solved\" board')
print_board(solved_board)
print()
print('Solution Board')
print_board(solution_board)
print()
same = solved_board == solution_board
print('Are solved and solution board the same?')
print(same)
