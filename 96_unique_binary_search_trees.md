# 96 - Unique Binary Search Trees

[leetcode link](https://leetcode.com/problems/unique-binary-search-trees/)

> Given *n*, how many structurally unique **BST's** (binary search trees) that store values 1 ... *n*?
>
> **Example:**
>
> ```
> Input: 3
> Output: 5
> Explanation:
> Given n = 3, there are a total of 5 unique BST's:
> 
>    1         3     3      2      1
>     \       /     /      / \      \
>      3     2     1      1   3      2
>     /     /       \                 \
>    2     1         2                 3
> ```
>
> **Constraints:**
>
> - `1 <= n <= 19`

## Recursive solution - TLE

```cpp
// 24/06/2020
int numTrees(int n) {
    if(n==0 || n==1) return 1;
    int count = 0;
    for(int left = 0; left<n; ++left)
        count += numTrees(left) * numTrees(n-1-left);
    return count;
}
```
## Dynamic Programming - O(n^2)

```cpp
// 24/06/2020
int numTrees(int n) {
    if(n==0) return 0;
    vector<int> dp(n+1);
    dp[0] = 1; dp[1] =1;
    for(int i = 2; i <=n; ++i)
        dp[i] = numtrees_dp(dp, i);
    return dp[n];
}

int numtrees_dp(const vector<int>& dp, int n){
    int count = 0;
    for(int left = 0; left<n; ++left)
        count += dp[left] * dp[n-1-left];
    return count;
}
```