# 59 - Spiral Matrix II

[leetcode link](https://leetcode.com/problems/spiral-matrix-ii/)

> Given a positive integer *n*, generate a square matrix filled with elements from 1 to *n*2 in spiral order.
>
> **Example:**
>
> ```
> Input: 3
> Output:
> [
>  [ 1, 2, 3 ],
>  [ 8, 9, 4 ],
>  [ 7, 6, 5 ]
> ]
> ```

## Solution

```cpp
// 20/02/2020
vector<vector<int>> generateMatrix(int n) {
    char direction = 0; 
    // 0 right
    // 1 down
    // 2 left
    // 3 up
    auto lines = vector<vector<int>>(n);
    for (auto& l: lines)
        l.resize(n, 0);
    int x = 0;
    int y = 0;
    for (int i = 1; i<=n*n; i++){
        lines[y][x] = i;
        bool change_direction = true;
        while (change_direction and i != n*n){
            change_direction = false;
            switch (direction){
            case 0:
                if (x < n-1 and lines[y][x+1] == 0)
                    x++;
                else{
                    direction = (direction+1)%4;
                    change_direction = true;
                }
                break;
            case 1:
                if (y < n-1 and lines[y+1][x] == 0)
                    y++;
                else{
                    direction = (direction+1)%4;
                    change_direction = true;
                }
                break;
            case 2:
                if (x > 0 and lines[y][x-1] == 0)
                    x--;
                else{
                    direction = (direction+1)%4;
                    change_direction = true;
                }
                break;
            case 3: 
                if (y > 0 and lines[y-1][x] == 0)
                    y--;
                else{
                    direction = (direction+1)%4;
                    change_direction = true;
                }
                break;
            }
        }
    }    
    return lines;
}
```