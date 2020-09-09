# 64 - Minimum Path Sum

[leetcode link](https://leetcode.com/problems/minimum-path-sum/)

> Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.
>
> **Note:** You can only move either down or right at any point in time.
>
> **Example:**
>
> ```
> Input:
> [
>   [1,3,1],
>   [1,5,1],
>   [4,2,1]
> ]
> Output: 7
> Explanation: Because the path 1→3→1→1→1 minimizes the sum.
> ```

## DP Solutions

```cpp
// 27/03/2020
int minPathSum(vector<vector<int>>& grid) {
    if (grid.size() == 0 || grid[0].size() == 0) return 0;
    auto h = grid.size();
    auto w = grid[0].size();
    vector<vector<int>> minsum(h, vector<int>(w, 0));
    // init bottom right corner
    minsum[h-1][w-1] = grid[h-1][w-1];
    // init bottom line
    for(int i = w-2; i >=0; i--)
        minsum[h-1][i] = grid[h-1][i] + minsum[h-1][i+1];
    // general case
    for(int j = h-2; j >= 0; j--){
        minsum[j][w-1] = grid[j][w-1] + minsum[j+1][w-1]; 
        for(int i = w-2; i >=0; i--){
            minsum[j][i] = grid[j][i] + min(minsum[j][i+1], minsum[j+1][i]); 
        }
    }
    return minsum[0][0];
}
```


```cpp
// 18/04/2020
int minPathSum(vector<vector<int>>& grid) {
    if (grid.size() == 0 || grid[0].size() == 0) return 0;
    vector<vector<int>> path(grid.size(), vector<int>(grid[0].size(), numeric_limits<int>::max()));
    int w = grid[0].size();
    for(int y = grid.size()-1; y>=0; y--){ 
        path[y][w-1] = grid[y][w-1] + (y == grid.size()-1?0:path[y+1][w-1]);
        for(int x = w-2; x>=0; x--){
            path[y][x] = min(path[y][x], grid[y][x] + path[y][x+1]);
            if(y != grid.size()-1)
                path[y][x] = min(path[y][x], grid[y][x] + path[y+1][x]);
        }
    }
    return path[0][0];
}
```