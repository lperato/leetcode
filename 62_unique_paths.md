# 62 - Unique Paths

[leetcode link](https://leetcode.com/problems/unique-paths/)

> A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).
>
> The robot can only move either down or right at any point in time.  The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
>
> How many possible unique paths are there?
>
> ![img](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
>  Above is a 7 x 3 grid. How many possible unique paths are there?
>
>  
>
> **Example 1:**
>
> ```
> Input: m = 3, n = 2
> Output: 3
> Explanation:
> From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
> 1. Right -> Right -> Down
> 2. Right -> Down -> Right
> 3. Down -> Right -> Right
> ```
>
> **Example 2:**
>
> ```
> Input: m = 7, n = 3
> Output: 28
> ```
>
>  
>
> **Constraints:**
>
> - `1 <= m, n <= 100`
> - It's guaranteed that the answer will be less than or equal to `2 * 10 ^ 9`.

## DP solution - O(m*n) time O(n) space

```cpp
// 29/06/2020
int uniquePaths(int m, int n) {
    vector<int> dp(n+1);
    dp[0] = 1;
    for(int j=0; j<m; ++j, dp[0]=0)
        for(int i=1; i<=n; ++i)
            dp[i] += dp[i-1];
    return dp[n];
}
```
## DP Solutions - O(m * n) time, O(m * n) time

```cpp
// 29/06/2020
int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m+1, vector<int>(n+1));
    dp[1][0] = 1;
    for(int j=1; j<=m; ++j){
        for(int i=1; i<=n; ++i)
            dp[j][i] = dp[j-1][i] + dp[j][i-1];
    }
    return dp[m][n];
}
```


```cpp
// 27/03/2020
int uniquePaths(int m, int n) {
    if (m==1)
        return 1;
    vector<vector<int>> nbpaths(n, vector<int>(m, 0));
    for(int y=0; y < n; y++){
        for(int x=0; x<m; x++){
            if (x == 0 || y == 0){
                nbpaths[y][x] = 1;
            }else{
                nbpaths[y][x] = nbpaths[y][x-1] + nbpaths[y-1][x];
            }
        }
    }
    return nbpaths[n-1][m-1];
}
```