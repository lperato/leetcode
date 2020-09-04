# 70 - Climbing Stairs

[leetcode link](https://leetcode.com/problems/climbing-stairs/)

## Recursion (TLE)

```cpp
// naive recursion => TLE
int climbStairs(int n) {
    if(n<=0) return n==0;
    return climbStairs(n-1) + climbStairs(n-2);
}
```
## Recursion + memoization

```cpp
// recursion plus memoization
int climbStairs(int n){
    vector<int> memo(n + 1, -1);
    memo[0] = 1;
    return climb_stairs(memo, n);
}

int climb_stairs(vector<int>& memo, int n){
    if(n<0) return 0;
    if(memo[n] == -1)
        memo[n] = climb_stairs(memo, n-1) + climb_stairs(memo, n-2);
    return memo[n];
}
```
## Dynamic Programming with O(1) space

### using 3 variables 

```cpp
// dp O(1) space with 3 variables
int climbStairs(int n) {
    if(n==0) return 0;
    if(n==1) return 1;
    if(n==2) return 2;
    int res=0, prev1=2, prev2 = 1;
    for(int i = 2; i <n; ++i){
        res = prev1 + prev2;
        prev2 = prev1;
        prev1 = res;
    }
    return res;
}
```
### using an array of 3 integers

```cpp
// dp O(1) space with array of 3 numbers
int climbStairs(int n) {
    if(n <= 2) return n;
    array<int, 3> dp{1, 2, 0};
    for(int i = 2; i < n; ++i){
        dp[2] = dp[0] + dp[1];
        dp[0] = dp[1];
        dp[1] = dp[2];
    }
    return dp[2];
}
```
