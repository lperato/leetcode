# 198 - House Robber

[leetcode link](https://leetcode.com/problems/house-robber/)

> You are a  professional robber planning to rob houses along a street. Each house  has a certain amount of money stashed, the only constraint stopping you  from robbing each of them is that adjacent houses have security system  connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.
>
> Given a list of non-negative integers representing the amount of  money of each house, determine the maximum amount of money you can rob  tonight **without alerting the police**.
>
> **Example 1:**
>
> ```
> Input: nums = [1,2,3,1]
> Output: 4
> Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
>              Total amount you can rob = 1 + 3 = 4.
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [2,7,9,3,1]
> Output: 12
> Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
>              Total amount you can rob = 2 + 9 + 1 = 12.
> ```
>
> **Constraints:**
>
> - `0 <= nums.length <= 100`
> - `0 <= nums[i] <= 400`

## Naïve recursion - TLE

```cpp
// 23/04/2020
// recursion - top down approach: TLE
int rob(vector<int>& nums) {
    return rob(nums.begin(), nums.end());
}
using IT = vector<int>::const_iterator;

int rob(IT begin, IT end){
    if(begin>=end) return 0;
    return max(*begin + rob(begin+2, end), rob(begin+1, end));
}
```
## Recursion + Memoization - O(n) time, O(n) space

```cpp
// 23/04/2020
// recursion + memoization
int rob(vector<int>& nums) {
    vector<int> cache(nums.size(), -1);
    return rob(nums, cache, 0, nums.size());
}

int rob(vector<int>&nums, vector<int>&cache, int begin, int end){
    if(begin>=end) return 0;
    if(cache[begin] == -1){
        cache[begin] = max(
            nums[begin] + rob(nums, cache, begin+2, end), 
            rob(nums, cache, begin+1, end));
    }
    return cache[begin];
}
```
## Dynamic programming - O(n) time, O(n) space

```cpp
// 21/08/2020
// dp - O(n) space
int rob(vector<int>& nums) {
    if(nums.empty()) return 0;
    vector<int> dp(nums.size());
    dp[0] = nums[0];
    for(int i = 1, size = nums.size(); i != size; ++i){
        dp[i] = max(nums[i] + (i>1?dp[i-2]:0), dp[i-1]);
    }
    return dp.back();
}
```
## Dynamic programming - O(n) time, O(1) space

```cpp
// 21/08/2020
// dp - O(1) space
int rob(vector<int>& nums) {
    if(nums.empty()) return 0;
    if(nums.size()<=2) return nums.size()==1?nums[0]:max(nums[0], nums[1]);
    array<int, 3> dp{nums[0], max(nums[0],nums[1]), 0};
    for(int i = 2, size = nums.size(); i < size; ++i, dp[0] = dp[1], dp[1] = dp[2])
        dp[2] = max(nums[i] + dp[0], dp[1]);
    return dp[2];
}
```