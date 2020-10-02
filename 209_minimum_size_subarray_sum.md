# 209 - Minimum Size Subarray Sum

[leetcode link](https://leetcode.com/problems/minimum-size-subarray-sum/)

> Given an array of **n** positive integers and a positive integer **s**, find the minimal length of a **contiguous** subarray of which the sum ≥ **s**. If there isn't one, return 0 instead.
>
> **Example:** 
>
> ```
> Input: s = 7, nums = [2,3,1,2,4,3]
> Output: 2
> Explanation: the subarray [4,3] has the minimal length under the problem constraint.
> ```
>
> **Follow up:**
>
> If you have figured out the *O*(*n*) solution, try coding another solution of which the time complexity is *O*(*n* log *n*). 

## Sliding window - O(n)

```cpp
// 29/09/2020
int minSubArrayLen(int s, vector<int>& nums) {
    int minlen = numeric_limits<int>::max();
    for(int l=0, r=0, size=nums.size(), sum = 0; r < size; ++r){
        sum += nums[r];
        while(sum >= s && l<=r){
            minlen = min(minlen, r-l+1);
            sum -= nums[l++];
        }
    }
    return minlen==numeric_limits<int>::max()?0:minlen;
}
```
### Ugly sliding window variant

```cpp
// 29/09/2020
int minSubArrayLen(int s, vector<int>& nums) {
    if(nums.empty()) return 0;
    int l = 0, r = 0, size = nums.size(), sum = nums[0], minlen = numeric_limits<int>::max();
    while(l<size){
        if(sum < s){
            if(++r == size)
                break;
            sum += nums[r];
        } else {
            minlen = min(minlen, r-l+1);
            if(l<r)
                sum -= nums[l++];
            else{
                ++r;
                ++l;
                if(r != size)
                    sum = nums[r];
            }
        }
    }
    return minlen==numeric_limits<int>::max()?0:minlen;
}
```