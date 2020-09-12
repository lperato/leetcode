# 152 - Maximum Product Subarray

[leetcode link](https://leetcode.com/problems/maximum-product-subarray/)

> Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.
>
> **Example 1:**
>
> ```
> Input: [2,3,-2,4]
> Output: 6
> Explanation: [2,3] has the largest product 6.
> ```
>
> **Example 2:**
>
> ```
> Input: [-2,0,-1]
> Output: 0
> Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
> ```

## O(n) solution

```cpp
int maxProduct(vector<int>& nums) {
    int maxprod = nums[0];
    for(int i = 1, minp = maxprod, maxp = minp; i != nums.size(); ++i){
        if(nums[i]<0)
            swap(minp, maxp);
        minp = min(nums[i], minp*nums[i]);
        maxp = max(nums[i], maxp*nums[i]);
        maxprod = max(maxprod, maxp);
    }
    return maxprod;
}
```
## Gab's solution - O(n)

```cpp
int maxProduct(const vector<int>& nums) {
    int running_max = 1, running_min = 1, max_prod = nums.front();
    for (const auto& n : nums) {
        int p1 = running_max * n, p2 = running_min * n; 
        running_max = max({p1, p2, n});
        running_min = min({p1, p2, n});
        max_prod = max(max_prod, running_max);
    }
    return max_prod;     
}
```