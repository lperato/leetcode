# 51 - N-Queens

[leetcode link](https://leetcode.com/problems/n-queens/)

> The *n*-queens puzzle is the problem of placing *n* queens on an *n*×*n* chessboard such that no two queens attack each other.
>
> ![img](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)
>
> Given an integer *n*, return all distinct solutions to the *n*-queens puzzle.
>
> Each solution contains a distinct board configuration of the *n*-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.
>
> **Example:**
>
> ```
> Input: 4
> Output: [
>  [".Q..",  // Solution 1
>   "...Q",
>   "Q...",
>   "..Q."],
> 
>  ["..Q.",  // Solution 2
>   "Q...",
>   "...Q",
>   ".Q.."]
> ]
> Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
> ```

## Backtracking solution

```cpp
// 06/09/2020
class Board{
    int n;
    vector<bool> rows; 
    vector<bool> asc_diags; 
    vector<bool> dsc_diags;
    vector<vector<bool>> board;
public:
    Board(int n): 
    n(n), rows(n), asc_diags(2*n-1), dsc_diags(2*n-1),
    board(n, vector<bool>(n)) {}
    
    void place(int r, int c, bool place = true){
        board[r][c] = place;
        rows[r] = place;
        asc_diags[r+c] = place;
        dsc_diags[r-c+size()] = place;
    }
    
    bool check(int r, int c) const {
        return !rows[r]
            && !asc_diags[r+c]
            && !dsc_diags[r-c+n];
    }
    
    inline int size() const {return n;}
    
    void copy_to(vector<string>& solution) const{
        for(int r = 0; r != n; ++r)
            for(int c = 0; c != n; ++c)
                if(board[r][c]) solution[r][c] = 'Q';
    }
};

using Solutions = vector<vector<string>>;
vector<vector<string>> solveNQueens(int n) {
    Board board(n);
    Solutions solutions;
    solve_n_queens(board, solutions);
    return solutions;
}

void solve_n_queens(Board& board, Solutions& solutions, int col = 0){
    if(col == board.size()){
        solutions.emplace_back(col, string(col, '.'));
        board.copy_to(solutions.back());
        return;
    }
    for(int r = 0, size = board.size(); r != size; ++r){
        if(board.check(r, col)){
            board.place(r, col);
            solve_n_queens(board, solutions, col+1);
            board.place(r, col, false);
        }
    }  
}
```
