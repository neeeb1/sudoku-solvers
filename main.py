# Define N matrix size (standard is 9x9)
N = 9

# A completed test puzzle
test_solution_string = "425971368173628594869543172241795836736182945958436721597864213384217659612359487"

# Same puzzle as solution, but missing entries.
test_puzzle_string = "405001068073628500009003070240790030006102005950000021507064213080217050612300007"

# Prints 2d array formatted puzzle as grid
def print_board(array):

    #null check
    if array == None:
        print("Can't print None !")
        return
    
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

    return(puzzle_array)
