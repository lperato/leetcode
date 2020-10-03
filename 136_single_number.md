# 136 - Single Number

[leetcode link](https://leetcode.com/problems/single-number/)

> Given a **non-empty** array of integers, every element appears *twice* except for one. Find that single one.
>
> **Note:**
>
> Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
>
> **Example 1:**
>
> ```
> Input: [2,2,1]
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: [4,1,2,1,2]
> Output: 4
> ```

## Solution - xor trick

```cpp
int singleNumber(vector<int>& nums) {
  return accumulate(next(nums.begin()), nums.end(), nums.front(), bit_xor<int>());
}
```