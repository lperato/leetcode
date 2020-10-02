# 41 - First Missing Positive

[leetcode link](https://leetcode.com/problems/first-missing-positive/)

>Given an unsorted integer array, find the smallest missing positive integer.
>
>**Example 1:**
>
>```
>Input: [1,2,0]
>Output: 3
>```
>
>**Example 2:**
>
>```
>Input: [3,4,-1,1]
>Output: 2
>```
>
>**Example 3:**
>
>```
>Input: [7,8,9,11,12]
>Output: 1
>```
>
>**Follow up:**
>
>Your algorithm should run in *O*(*n*) time and uses constant extra space.

## Cyclic sort - O(n)

*Pseudo algorithm :*
 1 - sort using cyclic sort and leave values out of range 
 2 - after sorting, scan for the index that does not have a sorted value

```cpp
// 30/09/2020
int firstMissingPositive(vector<int>& nums) {
    for(int i = 0; i < nums.size();){
        if(nums[i] != i+1 && nums[i] >= 1 && nums[i] < nums.size() +1 && nums[i] != nums[nums[i]-1])
            swap(nums[i], nums[nums[i]-1]);
        else ++i;
    }
    int i=0;
    while (i != nums.size() && nums[i] == i+1) ++i;
    return i+1;
}
```