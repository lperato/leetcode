# 137 - Single Number II

[leetcode link](https://leetcode.com/problems/single-number-ii/)

> Given a **non-empty** array of integers, every element appears *three* times except for one, which appears exactly once. Find that single one.
>
> **Note:**
>
> Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
>
> **Example 1:**
>
> ```
> Input: [2,2,3,2]
> Output: 3
> ```
>
> **Example 2:**
>
> ```
> Input: [0,1,0,1,0,1,99]
> Output: 99
> ```

## Solution

```cpp
int singleNumber(vector<int>& nums) {
    unordered_map<int, int8_t> seen;
    seen.reserve(nums.size());
    for(auto n:nums){
        auto it = seen.find(n);
        if(it == seen.end()){
            seen[n] = 1;
        }else{
            it->second++;
        }
    }
    for(const auto& it: seen)
        if(it.second == 1)
            return it.first;
    return -1;
}
```