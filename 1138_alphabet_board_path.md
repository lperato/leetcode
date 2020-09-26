# 1138 - Alphabet Board Path

[leetcode link](https://leetcode.com/problems/alphabet-board-path/)

> On an alphabet board, we start at position `(0, 0)`, corresponding to character `board[0][0]`.
>
> Here, `board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]`, as shown in the diagram below.
>
> ![img](https://assets.leetcode.com/uploads/2019/07/28/azboard.png)
>
> We may make the following moves:
>
> - `'U'` moves our position up one row, if the position exists on the board;
> - `'D'` moves our position down one row, if the position exists on the board;
> - `'L'` moves our position left one column, if the position exists on the board;
> - `'R'` moves our position right one column, if the position exists on the board;
> - `'!'` adds the character `board[r][c]` at our current position `(r, c)` to the answer.
>
> (Here, the only positions that exist on the board are positions with letters on them.)
>
> Return a sequence of moves that makes our answer equal to `target` in the minimum number of moves. You may return any path that does so.
>
> **Example 1:**
>
> ```
> Input: target = "leet"
> Output: "DDR!UURRR!!DDD!"
> ```
>
> **Example 2:**
>
> ```
> Input: target = "code"
> Output: "RR!DDRR!UUL!R!"
> ```
>
> **Constraints:**
>
> - `1 <= target.length <= 100`
> - `target` consists only of English lowercase letters.

## Solution

```cpp
// 26/09/2020
string alphabetBoardPath(string target) {
    int x = 0, y = 0;
    string moves;
    moves.reserve(target.size());
    for(auto c: target){
        int cx = (c-'a')%5, cy = (c-'a')/5;
        if(y!=5){
            moves.append(abs(cx-x), cx>x?'R':'L');
            moves.append(abs(cy-y), cy>y?'D':'U');
        }else{
            moves.append(abs(cy-y), cy>y?'D':'U');
            moves.append(abs(cx-x), cx>x?'R':'L');
        }
        moves.push_back('!');
        x = cx; y = cy;
    }
    return moves;
}
```