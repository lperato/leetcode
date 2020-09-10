# 45 - Jump Game II

[leetcode link](https://leetcode.com/problems/jump-game-ii/)

> Given an array of non-negative integers, you are initially positioned at the first index of the array.
>
> Each element in the array represents your maximum jump length at that position.
>
> Your goal is to reach the last index in the minimum number of jumps.
>
> **Example:**
>
> ```
> Input: [2,3,1,1,4]
> Output: 2
> Explanation: The minimum number of jumps to reach the last index is 2.
>     Jump 1 step from index 0 to 1, then 3 steps to the last index.
> ```
>
> **Note:**
>
> You can assume that you can always reach the last index.

## Solution 1 : naïve recursion - TLE

```cpp
// 10/09/2020
// recursive solution 1 : TLE
// hard to do memoization with it
int jump(vector<int>& nums) {
    int minjumps = nums.size();
    jump(nums, minjumps);
    return minjumps;
}

void jump(vector<int> nums, int& minjumps, int i = 0, int nbjump = 0){
    if(i >= nums.size()-1) {
        minjumps = min(minjumps, nbjump);
        return;
    }
    for(int j = 1; j <= nums[i]; ++j)
        jump(nums, minjumps, i+j, nbjump+1);
}
```
## Solution 2 : simpler recursion - TLE

```cpp
// 10/09/2020
// simpler recurive solution : TLE
int jump(vector<int>& nums, int i=0) {
    if(i >= nums.size()-1) return 0;
    int minjumps = nums.size();
    for(int j = 1; j <= nums[i]; ++j)
        minjumps = min(minjumps, 1 + jump(nums, i + j));
    return minjumps;
}
```
## Solution 3: recursion + memoization - TLE :-(

```cpp
// 10/09/2020
// recursion + memoization --> TLE
int jump(vector<int>& nums) {
    vector<int> memo(nums.size(), -1);
    return jump(nums, memo);
}

int jump(vector<int>& nums, vector<int>& memo, int i=0) {
    if(i == nums.size()-1) return 0;
    if(memo[i] == -1){
        int minjumps = nums.size();
        for(int j = 1, s = nums.size(); j <= nums[i] && i+j < s; ++j)
            minjumps = min(minjumps, 1 + jump(nums, memo, i + j));
        memo[i] = minjumps;
    }
    return memo[i];
}
```
## Solution 4 : Dynamic Programing 

```cpp
// 10/09/2020
// dp solution with pruning (maxreach)
int jump(vector<int>& nums) {
    vector<int> dp(nums.size(), nums.size());
    dp[0] = 0;
    int maxreach = 0;
    for(int i = 0, s = nums.size(); i != s; ++i){
        for(int j = maxreach+1; j <= i + nums[i] && j < s; ++j)
            dp[j] = min(dp[j], dp[i]+1);
        maxreach = i + nums[i];
    }
    return dp[nums.size()-1];
}
```
