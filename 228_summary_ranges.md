# 228 - Summary Ranges

[leetcode link](https://leetcode.com/problems/summary-ranges/)

> You are given a **sorted unique** integer array `nums`.
>
> Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.
>
> Each range `[a,b]` in the list should be output as:
>
> - `"a->b"` if `a != b`
> - `"a"` if `a == b`
>
> <...examples...>
>
> **Constraints:**
>
> - `0 <= nums.length <= 20`
> - `-231 <= nums[i] <= 231 - 1`
> - All the values of `nums` are **unique**.

## Solution: Sliding window - O(n)

```cpp
vector<string> summaryRanges(vector<int>& nums) {
    vector<string> result;
    for(int l = 0, r = 0, size = nums.size(); r != size; ++r){
        if(r == size-1 || nums[r+1] != nums[r]+1){
            string tmp;
            if(l == r)
                tmp = to_string(nums[l]);
            else
                tmp = to_string(nums[l]) + "->" + to_string(nums[r]);
            result.emplace_back(tmp);
            l = r+1;
        }
    }
    return result;
}
```