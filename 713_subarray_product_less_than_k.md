# 713 - Subarray Product Less Than K

[leetcode link](https://leetcode.com/problems/subarray-product-less-than-k/)

> Your are given an array of positive integers `nums`.
>
> Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than `k`.
>
> **Example 1:**
>
> ```
> Input: nums = [10, 5, 2, 6], k = 100
> Output: 8
> Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
> Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
> ```
>
> **Note:**
>
> `0 < nums.length <= 50000`.
>
> `0 < nums[i] < 1000`.
>
> `0 <= k < 10^6`.

## Sliding window

**TODO** Rework that solution to produce cleaner code

```cpp
// 28/09/2020
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
    int n = 0, l = 0, r = 0, p = nums[0], size = nums.size();
    while(r != size){
        if(p < k){
            n += r-l+1;
            ++r;
            if(r != size)
                p *= nums[r];
        } else {
            if(l < r)
                p /= nums[l++];
            else {
                ++l;
                ++r;
                if(r != size)
                    p = nums[r];
            }
        }
    }
    return n;   
}
```