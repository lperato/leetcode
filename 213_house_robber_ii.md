# 213 - House Robber II

[leetcode link](https://leetcode.com/problems/house-robber-ii/)

> You are a  professional robber planning to rob houses along a street. Each house  has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.
>
> Given a list of non-negative integers representing the amount of  money of each house, determine the maximum amount of money you can rob  tonight **without alerting the police**.
>
> **Example 1:**
>
> ```
> Input: [2,3,2]
> Output: 3
> Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
>              because they are adjacent houses.
> ```
>
> **Example 2:**
>
> ```
> Input: [1,2,3,1]
> Output: 4
> Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
>              Total amount you can rob = 1 + 3 = 4.
> ```

## Recursion + memoization - O(n) time, O(n) space

```cpp
// 21/08/2020
// recursion + memoization
int rob(vector<int>& nums) {
    vector<int> cache(nums.size(), -1);
    int rob0 = rob(nums, cache, 0, nums.size()==1?1:nums.size()-1);
    fill(cache.begin(), cache.end(), -1);
    return max(rob0, rob(nums, cache, 1, nums.size()));
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
## Dynamic programming - O(n) time, O(1) space

```cpp
// 21/08/2020
// dp - O(1) space
using IT = vector<int>::const_iterator;
int rob(vector<int>& nums) {
    if(nums.empty()) return 0;
    if(nums.size() == 1) return nums[0];
    return max( rob(nums.begin(), prev(nums.end())),
                rob(nums.begin()+1, nums.end()));
}

int rob(IT begin, IT end) {
    if(begin >= end) return 0;
    if(end - begin <=2) return end==begin+1?*begin:max(*begin, *(begin+1));
    array<int, 3> dp{*begin, max(*begin, *(begin+1)), 0};
    for(auto it = begin+2; it != end; ++it, dp[0] = dp[1], dp[1] = dp[2])
        dp[2] = max(*it + dp[0], dp[1]);
    return dp[2];
}
```
