# 79 - Word Search

[leetcode link](https://leetcode.com/problems/word-search/)

> Given a 2D board and a word, find if the word exists in the grid.
>
> The word can be constructed from letters of sequentially adjacent  cell, where "adjacent" cells are those horizontally or vertically  neighboring. The same letter cell may not be used more than once.
>
> **Example:**
>
> ```
> board =
> [
>   ['A','B','C','E'],
>   ['S','F','C','S'],
>   ['A','D','E','E']
> ]
> 
> Given word = "ABCCED", return true.
> Given word = "SEE", return true.
> Given word = "ABCB", return false.
> ```
>
> **Constraints:**
>
> - `board` and `word` consists only of lowercase and uppercase English letters.
> - `1 <= board.length <= 200`
> - `1 <= board[i].length <= 200`
> - `1 <= word.length <= 10^3`

## Solution

```cpp
// 31/03/2020
bool exist(vector<vector<char>>& board, string word) {
    if(board.empty() || word.empty())
        return false;
    int w = board[0].size();
    for(int y = 0; y < board.size(); y++){
        for(int x = 0; x < w; x++){
            if (board[y][x] == word[0]){
                if (exist(board, x, y, word.begin()+1, word.end()))
                    return true;
            }
        }
    }
    return false;
}

bool exist(vector<vector<char>>& board, int x, int y, string::const_iterator begin, string::const_iterator end){
    if(begin == end)
        return true;
    auto tmp = board[y][x];
    board[y][x] = 0;
    int w = board[0].size();
    bool res = false;
    if ((x<w-1 && board[y][x+1] == *begin && exist(board, x+1, y, begin+1, end))
    || (x>0 && board[y][x-1] == *begin && exist(board, x-1, y, begin+1, end))
    || (y<board.size()-1 && board[y+1][x] == *begin && exist(board, x, y+1, begin+1, end))
    || (y>0 && board[y-1][x] == *begin && exist(board, x, y-1, begin+1, end)))
        res = true;
    board[y][x] = tmp;
    return res;
}
```