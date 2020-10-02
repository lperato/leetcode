# 315 - Count of Smaller Numbers After Self

[leetcode link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

> You are given an integer array *nums* and you have to return a new *counts* array. The *counts* array has the property where `counts[i]` is the number of smaller elements to the right of `nums[i]`.
>
> **Example 1:**
>
> ```
> Input: nums = [5,2,6,1]
> Output: [2,1,1,0]
> Explanation:
> To the right of 5 there are 2 smaller elements (2 and 1).
> To the right of 2 there is only 1 smaller element (1).
> To the right of 6 there is 1 smaller element (1).
> To the right of 1 there is 0 smaller element.
> ```
>
> **Constraints:**
>
> - `0 <= nums.length <= 10^5`
> - `-10^4 <= nums[i] <= 10^4`

## Solution 1: incremental sort using a multiset - O(n^2) - TLE 

```cpp
// 29/09/20202
vector<int> countSmaller(vector<int>& nums) {
    multiset<int, greater<int>> seen; 
    vector<int> result(nums.size());
    for(int i = nums.size()-1; i >= 0; --i){
        if(auto it_less = seen.upper_bound(nums[i]); it_less != seen.end())
            result[i] = distance(it_less, seen.end());
        seen.insert(nums[i]);
    }
    return result;
}
```
## Solution 2: incremental sort within the input array - O(n^2) - accepted but slow 

```cpp
// 29/09/20202
vector<int> countSmaller(vector<int>& nums) {
    vector<int> result(nums.size());
    for(int i = nums.size()-1; i >= 0; --i){
        auto it = lower_bound(nums.begin()+i+1, nums.end(), nums[i]);
        result[i] = it - (nums.begin() + i +1);
        if(it != nums.begin()+i+1){
            int tmp = nums[i];
            copy(nums.begin()+i+1, it, nums.begin()+i);
            *prev(it)=tmp;
        }
    }
    return result;
}
```
**TODO:**

	- solution implementing binary tree
	- solution using merge sort

