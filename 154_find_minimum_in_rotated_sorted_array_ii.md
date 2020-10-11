# 154 - Find Minimum in Rotated Sorted Array II

[leetcode link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

> Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
>
> (i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).
>
> Find the minimum element.
>
> The array may contain duplicates.
>
> **Example 1:**
>
> ```
> Input: [1,3,5]
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: [2,2,2,0,1]
> Output: 0
> ```
>
> **Note:**
>
> - This is a follow up problem to [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/).
> - Would allow duplicates affect the run-time complexity? How and why?

## STL Lol solution - O(n)

```cpp
//25/07/2020
int findMin(vector<int>& nums) {
    return *min_element(nums.begin(), nums.end());
}
```
## Binary search - O(log(n))

```cpp
// 25/07/2020
int findMin(vector<int>& nums) {
    return find_min(nums, 0, nums.size(), nums[0]);
}

int find_min(const vector<int>& nums, int i, int j, int minval) {
    while(i<j){
        int mid = i+(j-i)/2;
        if(nums[mid] == minval){
            return min(
                find_min(nums, i, mid, minval),
                find_min(nums, mid+1, j, minval));
        } else if(nums[mid] < minval) {
            minval = nums[mid];
            j = mid;
        } else i = mid+1;
    }
    return minval;
}
```