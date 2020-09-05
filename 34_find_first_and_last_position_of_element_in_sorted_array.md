# 34 - Find First and Last Position of Element in Sorted Array

[leetcode link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

> Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target` value.
>
> Your algorithm's runtime complexity must be in the order of *O*(log *n*).
>
> If the target is not found in the array, return `[-1, -1]`.
>
> **Example 1:**
>
> ```
> Input: nums = [5,7,7,8,8,10], target = 8
> Output: [3,4]
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [5,7,7,8,8,10], target = 6
> Output: [-1,-1]
> ```
>
>  
>
> **Constraints:**
>
> - `0 <= nums.length <= 10^5`
> - `-10^9 <= nums[i] <= 10^9`
> - `nums` is a non decreasing array.
> - `-10^9 <= target <= 10^9`

## BinarySearch with equal_range (Gab's solution) - O(log(n)) - Know your STL!

```cpp
vector<int> searchRange(vector<int>& nums, int target) {
    auto [lower, upper] = equal_range(nums.cbegin(), nums.cend(), target);
    if (lower != nums.cend() && *lower == target)
        return {int(lower - nums.cbegin()), int(upper - nums.cbegin() - 1)};
    return {-1, -1};
}
```

## BinarySearch with lower_bound O(log(n)) 

For some reason, this is not achieving better results than solution 2

```cpp
// 05/09/2020
vector<int> searchRange(vector<int>& nums, int target) {
    auto it = lower_bound(nums.begin(), nums.end(), target);
    if(it == nums.end() || *it != target)
        return {-1, -1};
    int i = it - nums.begin(), j = i+1, size = nums.size();
    while(j != size && nums[j] == target)++j;
    return {i, j-1};
}
```
## Solution 2 - O(n)

```cpp
// 27/02/2020
vector<int> searchRange(vector<int>& nums, int target) {
    int i;
    for(i = 0; i < nums.size() && nums[i]!= target; i++);
    if (i == nums.size())
        return vector<int>{-1, -1};
    int begin = i;
    for(; i < nums.size() && nums[i]== target; i++);
    return vector<int>{begin, i-1};
}
```


