# 55 - Jump Game

[leetcode link](https://leetcode.com/problems/jump-game/)

> Given an array of non-negative integers, you are initially positioned at the first index of the array.
>
> Each element in the array represents your maximum jump length at that position.
>
> Determine if you are able to reach the last index.
>
>  
>
> **Example 1:**
>
> ```
> Input: nums = [2,3,1,1,4]
> Output: true
> Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [3,2,1,0,4]
> Output: false
> Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
> ```
>
>  
>
> **Constraints:**
>
> - `1 <= nums.length <= 3 * 10^4`
> - `0 <= nums[i][j] <= 10^5

   ## Solutions

```cpp
// 12/08/2020
bool canJump(vector<int>& nums) {
   int max_reach = 0;
   for(int i = 0; i <= max_reach && max_reach < nums.size(); ++i)
       max_reach = max(max_reach, i+nums[i]);
   return max_reach >= nums.size()-1;
}
```


```cpp
// 07/03/2020
bool canJump(vector<int>& nums) {
    int max_reach = 0;
    for(int i = 0; i<=max_reach && i < nums.size(); i++){
        if (i + nums[i]>max_reach)
            max_reach = i + nums[i];
    }
    return max_reach >= nums.size() - 1;
}
```

