import check
import main
import simple_backtrack

#Calculates list of possible solutions in a given space given a 2d puzzle array, x, and y coords 
def calculate_candidates(puzzle, row, col):
    legal_list = []
    for number in range(1, main.N+1):
        if check.is_legal(puzzle, row, col, number):
            legal_list.append(number)
    return legal_list

# def fill_single_empty(puzzle_array):
#     for row in range(main.N):
#         col_members = []
#         for col in range(main.N):
#             col_members.append(puzzle_array[row][col])
#         print(col_members)
#         if col_members.count(0) == 1:
#             print("This one!!!")
#             start = col_members[0]
#             end = col_members[-1]
#             missing = sorted(set(range(start, end +1)).difference(col_members))
#             print(missing)
#             puzzle_array[row][col_members.index(0)] = missing[0]

#     print()

#     for col in range(main.N):
#         row_members = []
#         for row in range(main.N):
#             row_members.append(puzzle_array[row][col])
#         print(row_members)
#         if row_members.count(0) == 1:
#             print("This one!!!")
#             start = row_members[0]
#             end = row_members[-1]
#             missing = sorted(set(range(start, end +1)).difference(row_members))
#             print(missing)
#             puzzle_array[row_members.index(0)][col] = missing[0]
    
#     return puzzle_array

def insert_solo_candidates(puzzle_array):
    # Iterates over rows and columns
    for row in range(main.N):
        for col in range(main.N):
            if puzzle_array[row][col] == 0 and len(calculate_candidates(puzzle_array, row, col)) == 1:
                puzzle_array[row][col] = calculate_candidates(puzzle_array, row, col)[0]
    
    return puzzle_array

def candidate_solve(puzzle_array):
    puzzle_array = insert_solo_candidates(puzzle_array)
    return simple_backtrack.backtrack_solve(puzzle_array)

# puzzle = main.puzzle_string_to_array(main.test_puzzle_string)
# main.print_board(puzzle)

# puzzle = insert_solo_candidates(puzzle)
# main.print_board(puzzle)

# main.print_board(fill_single_empty(puzzle))