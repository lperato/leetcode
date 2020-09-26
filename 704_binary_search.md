# 704 - Binary Search

[leetcode link](https://leetcode.com/problems/binary-search/)

> Given a **sorted** (in ascending order) integer array `nums` of `n` elements and a `target` value, write a function to search `target` in `nums`. If `target` exists, then return its index, otherwise return `-1`.
>
> 
>  **Example 1:**
>
> ```
> Input: nums = [-1,0,3,5,9,12], target = 9
> Output: 4
> Explanation: 9 exists in nums and its index is 4
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [-1,0,3,5,9,12], target = 2
> Output: -1
> Explanation: 2 does not exist in nums so return -1
> ```
>
> **Note:**
>
> 1. You may assume that all elements in `nums` are unique.
> 2. `n` will be in the range `[1, 10000]`.
> 3. The value of each element in `nums` will be in the range `[-9999, 9999]`.

## Iterative solution

```cpp
// 18/09/2020
// iterative solution
int search(vector<int>& nums, int target) {
    int l = 0, r = nums.size();
    while(l<r){
        int mid = l+(r-l)/2;
        if(nums[mid]<target)
            l = mid +1;
        else if(nums[mid]>target)
            r = mid;
        else
            return mid;
    }
    return -1;
}
```
## Recursive solution

```cpp
// 18/09/2020
// recursive solution
int search(vector<int>& nums, int target) {
    return search(nums, target, 0, nums.size());
}

int search(vector<int>& nums, int target, int l, int r){
    if (l>=r) 
        return -1;
    int mid = l+(r-l)/2;
    if (nums[mid]<target)
        return search(nums, target, mid +1, r);
    else if (nums[mid]>target)
        return search(nums, target, l, mid);
    else
        return mid;
}
```
## TODO : solutions with iterators