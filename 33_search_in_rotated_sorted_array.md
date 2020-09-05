# 33 - Search in Rotated Sorted Array

[leetcode link](https://leetcode.com/problems/search-in-rotated-sorted-array/)

> You are given an integer array `nums` sorted in ascending order, and an integer `target`.
>
> Suppose that `nums` is rotated at some pivot unknown to you beforehand (i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).
>
> *If `target` is found in the array return its index, otherwise, return `-1`.*
>
>  
>
> **Example 1:**
>
> ```
> Input: nums = [4,5,6,7,0,1,2], target = 0
> Output: 4
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [4,5,6,7,0,1,2], target = 3
> Output: -1
> ```
>
> **Example 3:**
>
> ```
> Input: nums = [1], target = 0
> Output: -1
> ```
>
>  
>
> **Constraints:**
>
> - `1 <= nums.length <= 5000`
> - `-10^4 <= nums[i] <= 10^4`
> - All values of `nums` are **unique**.
> - `nums` is guranteed to be rotated at some pivot.
> - `-10^4 <= target <= 10^4`

## Solution 

```cpp
// 28/02/2020
int search(vector<int>& nums, int target) {
    return rotated_search(nums, 0, nums.size()-1, target);
}

int rotated_search(const vector<int>& nums, 
                  int begin, int end, int target){
    if (end == -1)
        return -1;
    if (begin == end){
        return nums[begin]==target?begin:-1; 
    }
    if(nums[begin] < nums[end]){
        return binary_search(nums, begin, end, target);
    }
    if(begin == end-1){
        if (target == nums[begin])
            return begin;
        if (target == nums[end])
            return end;
        return -1;
    }
    int mid = begin + (end - begin) / 2;
    int s1 = rotated_search(nums, begin, mid, target);
    if (s1 != -1)
        return s1;
    return rotated_search(nums, mid, end, target);
}

int binary_search(const vector<int>& nums, 
                  int begin, int end, int target){
    if (begin == end){
        return nums[begin]==target?begin:-1; 
    }
    
    if(begin == end-1){
        if (target == nums[begin])
            return begin;
        if (target == nums[end])
            return end;
        return -1;
    }
    
    int mid = begin + (end - begin) / 2;
    //cout << "mid: " << mid << ":"<<nums[mid]<<"\n"; 
    if(target<nums[mid]){
        return binary_search(nums, begin, mid, target);
    }
    else{
        return binary_search(nums, mid, end, target);
    }   
}
```