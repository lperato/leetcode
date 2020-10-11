# 169 - Majority Element

[leetcode link](https://leetcode.com/problems/majority-element/)

> Given an array of size *n*, find the majority element. The majority element is the element that appears **more than** `⌊ n/2 ⌋` times.
>
> You may assume that the array is non-empty and the majority element always exist in the array.
>
> **Example 1:**
>
> ```
> Input: [3,2,3]
> Output: 3
> ```
>
> **Example 2:**
>
> ```
> Input: [2,2,1,1,1,2,2]
> Output: 2
> ```

## Solution 1: hashmap - O(n) space

```cpp
// 16/03/2020
int majorityElement(vector<int>& nums) {
    unordered_map<int, int> count;
    for(auto n: nums){
        auto it = count.find(n);
        if (it == count.end()){
            count.insert(pair<int, int>(n, 1));
        } else {
            it->second++;
        }
    }
    for (auto it: count){
        if(it.second > nums.size()/2)
            return it.first;
    }
    return -1;
}
```
## Solution 2: Boyer Moore vote algorithm - O(1) space

```cpp
// 28/07/2020
int majorityElement(vector<int>& nums) {
    int elt;
    for(int i = 0, s = 0, size=nums.size(); i < size; ++i){
        if(s == 0) elt = nums[i];
        s += nums[i] == elt?1:-1;
    }
    return elt;
}
```
### Variant

```cpp
// 28/07/2020
int majorityElement(vector<int>& nums) {
    int elt = nums[0];
    for(int i = 1, s = 1, size=nums.size(); i < size; ++i){
        s += nums[i] == elt?1:-1;
        if(s == 0 && i != size)
            elt = nums[i+1];
    }
    return elt;
}
```