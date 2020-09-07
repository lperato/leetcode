# 52 - N-Queens II

[leetcode link](https://leetcode.com/problems/n-queens-ii/)

> The *n*-queens puzzle is the problem of placing *n* queens on an *n*×*n* chessboard such that no two queens attack each other.
>
> ![img](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)
>
> Given an integer *n*, return the number of distinct solutions to the *n*-queens puzzle.

## Backtracking solution

```cpp
class Board{
    int n;
    vector<bool> rows; 
    vector<bool> asc_diags; 
    vector<bool> dsc_diags;
public:
    Board(int n): n(n), rows(n), asc_diags(2*n-1), dsc_diags(2*n-1) {}
    void place(int r, int c, bool place = true){
        rows[r] = place;
        asc_diags[r+c] = place;
        dsc_diags[r-c+size()] = place;
    }
    bool check(int r, int c) const {
        return !rows[r] && !asc_diags[r+c] && !dsc_diags[r-c+n];
    }
    inline int size() const {return n;}
};

int totalNQueens(int n) {
    Board board(n);
    return n_queens(board);
}

int n_queens(Board& board, int col = 0){
    if(col == board.size()) return 1;
    int nbsol = 0;
    for(int r = 0, size = board.size(); r != size; ++r){
        if(board.check(r, col)){
            board.place(r, col);
            nbsol += n_queens(board, col+1);
            board.place(r, col, false);
        }
    }
    return nbsol;    
}
```
### Fun with RAII/CADR

For more fun, we can have a `ScopedPlacement` class:

```cpp
class ScopedPlacement{
    Board& board; 
    int r; 
    int c;
public:
    ScopedPlacement(Board& board, int r, int c):board(board), r(r), c(c){board.place(r, c);}
    ~ScopedPlacement(){board.place(r, c, false);}
};
```
Then the black-tracked placement code becomes:

```cpp
if(board.check(r, col)){
    ScopedPlacement placement(board, r, col); 
    nbsol += n_queens(board, col+1);
}
```
❤️