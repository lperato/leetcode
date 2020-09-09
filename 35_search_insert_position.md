# 35 - Search Insert Position

[leetcode link](https://leetcode.com/problems/search-insert-position/)

> Given a sorted array and a target value, return the index if the target is found. If  not, return the index where it would be if it were inserted in order.
>
> You may assume no duplicates in the array.
>
> **Example 1:**
>
> ```
> Input: [1,3,5,6], 5
> Output: 2
> ```
>
> **Example 2:**
>
> ```
> Input: [1,3,5,6], 2
> Output: 1
> ```
>
> **Example 3:**
>
> ```
> Input: [1,3,5,6], 7
> Output: 4
> ```
>
> **Example 4:**
>
> ```
> Input: [1,3,5,6], 0
> Output: 0
> ```

## Linear search - O(n)

### Manual iterator version

```cpp
// 27/02/2020 
int searchInsert(vector<int>& nums, int target) {
    auto it = nums.begin();
    while(it != nums.end() && *it<target)++it;
    return it - nums.begin();
}
```
## Binary search - O(log(n)) 

### STL version

```cpp
// 09/09/2020 
int searchInsert(vector<int>& nums, int target){
    return lower_bound(nums.begin(), nums.end(), target)-nums.begin();
}
```

### Iterator version

```cpp
// 10/06/2020
int searchInsert(vector<int>& nums, int target){
    auto begin = nums.begin(), end = nums.end();
    while(begin != end){
        auto mid = begin + ((end - begin) >> 1);
        if(target <= *mid)
            end = mid;
        else
            begin = mid+1;
    }
    return begin-nums.begin();
}
```
### [] operator version

```cpp
// 10/06/2020
int searchInsert(vector<int>& nums, int target){
    size_t begin = 0, end = nums.size();
    while(begin < end){
        auto mid = begin + ((end - begin) >> 1);
        if(target <= nums[mid])
            end = mid;
        else
            begin = mid+1;
    }
    return begin;
}
```