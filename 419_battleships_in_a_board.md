# 419 - Battleships in a Board

[leetcode link](https://leetcode.com/problems/battleships-in-a-board/)

> Given an 2D board, count how many battleships are in it. The battleships are represented with `'X'`s, empty slots are represented with `'.'`s. You may assume the following rules:
>
> - You receive a valid board, made of only battleships or empty slots.
> - Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape `1xN` (1 row, N columns) or `Nx1` (N rows, 1 column), where N can be of any size.
> - At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

## solution O(1) memory that modify the board

```cpp
// 03/09/2020
int countBattleships(vector<vector<char>>& board) {
    if(board.empty()) return 0;
    int n = 0;
    for(int y=0, sy=board.size(), sx=board[0].size(); y != sy; ++y){
        for(int x = 0; x != sx; ++x){
            if(board[y][x]=='X'){
                ++n;
                board[y][x]='x';
                if (x!=sx-1 && board[y][x+1] == 'X')
                    for(int i = x+1; i != sx && board[y][i] == 'X'; board[y][i++] = 'x');
                else if(y!=sy-1 && board[y+1][x] == 'X')
                    for(int i = y+1; i != sy && board[i][x] == 'X'; board[i++][x] = 'x');
            }
        }
    }
    return n;
}
```

## solution O(1) memory without modifying the board

```cpp
// 03/09/2020
int countBattleships(vector<vector<char>>& board) {
    if(board.empty()) return 0;
    int n = 0;
    for(int y=0, sy=board.size(), sx=board[0].size(); y != sy; ++y)
        for(int x = 0; x != sx; ++x)
            n += (board[y][x]=='X' 
                  && (x == 0 || board[y][x-1]!='X')
                  && (y == 0 || board[y-1][x]!='X'));
    return n;
}
```

