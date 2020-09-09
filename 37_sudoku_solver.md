# 37 - Sudoku Solver

[leetode link](https://leetcode.com/problems/sudoku-solver/)

> Write a program to solve a Sudoku puzzle by filling the empty cells.
>
> A sudoku solution must satisfy **all of the following rules**:
>
> 1. Each of the digits `1-9` must occur exactly once in each row.
> 2. Each of the digits `1-9` must occur exactly once in each column.
> 3. Each of the the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.
>
> Empty cells are indicated by the character `'.'`.
>
> ![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
>  A sudoku puzzle...
>
> ![img](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)
>  ...and its solution numbers marked in red.
>
> **Note:**
>
> - The given board contain only digits `1-9` and the character `'.'`.
> - You may assume that the given Sudoku puzzle will have a single unique solution.
> - The given board size is always `9x9`.

## Backtracking solution

```cpp
// 08/09/2020
class SudokuBoard{
    char grid[9][9];
    bool row[9][10];
    bool col[9][10];
    bool square[3][3][10];
public:
    SudokuBoard():grid(),row(),col(),square() {}
    void set(int r, int c, char val) {
        char oldval = grid[r][c];
        grid[r][c] = val;
        row[r][oldval] = false;
        col[c][oldval] = false;
        square[r/3][c/3][oldval] = false;
        row[r][val] = (bool)val;
        col[c][val] = (bool)val;
        square[r/3][c/3][val] = (bool)val;
    }
    bool check(int r, int c, int val) const {
        return !row[r][val] && !col[c][val] && !square[r/3][c/3][val];
    }
    const char& get(int r, int c) const {return grid[r][c];}
};

void solveSudoku(vector<vector<char>>& board) {
    SudokuBoard b;
    vector<pair<int, int>> to_solve;
    for(int r = 0; r != 9; ++r){
        for(int c = 0; c != 9; ++c){
            if(board[r][c] == '.')
                to_solve.emplace_back(r, c);
            else
                b.set(r, c, board[r][c] - '0');
        }
    }
    solve_sudoku(b, to_solve);
    for(int r = 0; r != 9; ++r)
        for(int c = 0; c != 9; ++c)
            board[r][c] = b.get(r, c) + '0';
}

bool solve_sudoku(SudokuBoard& board, const vector<pair<int, int>>& to_solve, int i = 0){
    if(i == to_solve.size())
        return true;
    auto [r, c] = to_solve[i];
    for (int val = 1; val != 10; ++val){
        if(board.check(r, c, val)){
            board.set(r, c, val);
            if(solve_sudoku(board, to_solve, i+1))
                return true;
            board.set(r, c, 0);
        }
    }
    return false;
}
```