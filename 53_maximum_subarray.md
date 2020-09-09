# 53 - Maximum Subarray

[leetcode link](https://leetcode.com/problems/maximum-subarray/)

> Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.
>
> **Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.
>
>  
>
> **Example 1:**
>
> ```
> Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
> Output: 6
> Explanation: [4,-1,2,1] has the largest sum = 6.
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [1]
> Output: 1
> ```
>
> **Example 3:**
>
> ```
> Input: nums = [0]
> Output: 0
> ```
>
> **Example 4:**
>
> ```
> Input: nums = [-1]
> Output: -1
> ```
>
> **Example 5:**
>
> ```
> Input: nums = [-2147483647]
> Output: -2147483647
> ```

**TODO** add explanation to solutions

## Solution 1 - O(n)

```cpp
// 12/08/2020 approach using sum[i -> j] = sum[0->j] - sum[0->i]
int maxSubArray(vector<int>& nums) {
    int maxsum = nums[0];
    for(int i = 0, sz = nums.size(), sum=0, minsum=0; i != sz; ++i){
        sum += nums[i];
        maxsum=max(maxsum, sum-minsum);
        minsum=min(minsum, sum);
    }
    return maxsum;
}
```

## Solution 2 - O(n)

```cpp
// 27/02/2020
int maxSubArray(vector<int>& nums) {
    if(nums.size()==1)
        return nums[0];
    int sum; 
    int max; 
    for(int i = 0; i < nums.size(); i++){
        if(i == 0){
            sum = nums[i];
            max = sum;
        }
        else
            sum += nums[i];
        if(sum > max)
            max = sum;
        if (sum < 0)
            sum = 0;
    }
    return max;
}
```
