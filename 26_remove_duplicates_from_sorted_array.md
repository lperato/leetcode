# 26 - Remove Duplicates from Sorted Array

[leetcode link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

> Given a sorted array *nums*, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each element appear only *once* and return the new length.
>
> Do not allocate extra space for another array, you must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.
>
> It doesn't matter what values are set beyond the returned length.

## Solution 1 : Know your STL

```cpp
// 26/07/2020
int removeDuplicates(vector<int>& nums) {
    nums.erase(unique(nums.begin(), nums.end()), nums.end());
    return nums.size();
}
```
## Solution 2 : Reinvent the wheel

```cpp
// 25/02/2020
int removeDuplicates(vector<int>& nums) {
    return my_unique(nums.begin(), nums.end()) - nums.begin();
    // or
    // nums.erase(my_unique(nums.begin(), nums.end()), nums.end());
    //return nums.size();
}

using It = vector<int>::iterator;
vector<int>::iterator my_unique(It begin, It end){
    if (begin == end) return begin;
    for(auto it = begin+1; it != end; ++it)
        if (*it!=*begin)
            *++begin = *it;
    return begin+1;
}
```
