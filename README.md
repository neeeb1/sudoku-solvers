# Comparing and Optimizing Sudoku Solvers

This project was meant as a learning exercise for myself. 

I complete a sudoku puzzle for myself everyday as part of a daily puzzle solving routine to help my mental sharpness and jumpstart my brain first thing in the morning. Also, because I just think they're neat. 

I've also been learning python, which inspired me to study Backtracking Algorithms for solving sudoku puzzles. 

## Sudoku Puzzles

Sudoku puzzles are a strain of Constraint Satisfaction Problems where a grid, typically of size 9x9, is filled with numbers 1 through 9 following a few rules:

- Each row or column in the grid can only contain one instance of each number (aka no repeats)
- The puzzle is broken into sub-grids of 3x3 size, which can also only contain one instance of each number
- Each space must be filled with a number



I utilized the [9 Million Sudoku Puzzles and Solutions](https://www.kaggle.com/datasets/rohanrao/sudoku) dataset on Kaggle, published by vopani, for testing and benchmarking. In this dataset, each puzzle is represented by a string of 81 digits with empty spaces represented as 0.

## Solving the Sudoku

The simplest backtracking algorithm is quick, but by narrowing solutions before beginning recursion, we can speed up the brute-force process of backtracking. In this project, I did this by creating a "candidate" solve method.

The candidate solve method creates a list of legal numbers for every space. If a space has only one legal solution, or a list of length n = 1, that space can be filled with it's solution. This cut average solving time for 10,000 puzzles by about half (from ~70 )

## Todo:

I'd like to further extend this optimization in the future, implementing advanced tricks that many competitive and speed sudoku solvers use including:

- [Naked Pairs](https://www.learn-sudoku.com/naked-pairs.html) to narrow solutions down when two spaces in a sub-square have the same set of candidate solutions
- [Hidden Pairs](https://www.learn-sudoku.com/hidden-pairs.html), which are naked pairs that are "hidden" with extra candidate solutions
- The [X Wing](https://www.learn-sudoku.com/x-wing.html) technique