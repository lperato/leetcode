# 63 - Unique Paths II

[leetcode link](https://leetcode.com/problems/unique-paths-ii/)

> A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).
>
> The robot can only move either down or right at any point in time.  The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
>
> Now consider if some obstacles are added to the grids. How many unique paths would there be?
>
> ![img](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
>
> An obstacle and empty space is marked as `1` and `0` respectively in the grid.
>
> **Note:** *m* and *n* will be at most 100.
>
> **Example 1:**
>
> ```
> Input:
> [
>   [0,0,0],
>   [0,1,0],
>   [0,0,0]
> ]
> Output: 2
> Explanation:
> There is one obstacle in the middle of the 3x3 grid above.
> There are two ways to reach the bottom-right corner:
> 1. Right -> Right -> Down -> Down
> 2. Down -> Down -> Right -> Right
> ```

## DP Solution - O(m*n) time, O(n) space

```cpp
// 29/06/2020
int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
   auto m = obstacleGrid.size();
   auto n = obstacleGrid[0].size();
   vector<int> dp(n+1);
   dp[0] = 1;
   for(int j=0; j<m; ++j, dp[0]=0)
       for(int i=1; i<=n; ++i)
           dp[i] = obstacleGrid[j][i-1]?0: dp[i] + dp[i-1];
   return dp[n];
}
```