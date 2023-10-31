import csv
import time

import simple_backtrack
import assumption_backtrack
import main

print("Loading test cases....\n")

with open('sudoku.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)

    cases = []
    i = 0
    for row in reader:
          cases.append(row)
          i+=1
          if i >= 10000:
               break

print(f"{len(cases)} cases loaded.\n")

print("Starting backtracking algorithim on all test cases... \n")

count = 0
failed = 0

start = time.time()
for pair in cases:
     puzzle = pair["puzzle"]
     solution = pair["solution"]

     result = simple_backtrack.backtrack_solve(main.puzzle_string_to_array(puzzle))
     
     if result != main.puzzle_string_to_array(solution):
          print (f"Failed case #{count}")
          failed += 1
          
     count += 1

end = time.time()
print(f"{count} test cases completed in {end - start} seconds. \n{failed} test cases failed. \n{count - failed} test cases successful.\n\n")





print("Starting candidate algorithim on all test cases... \n")

count = 0
failed = 0

start = time.time()
for pair in cases:
     puzzle = pair["puzzle"]
     solution = pair["solution"]

     result = assumption_backtrack.candidate_solve(main.puzzle_string_to_array(puzzle))
     
     if result != main.puzzle_string_to_array(solution):
          print (f"Failed case #{count}")
          failed += 1
          
     count += 1

end = time.time()
print(f"{count} test cases completed in {end - start} seconds. \n{failed} test cases failed. \n{count - failed} test cases successful. \n\n")

