# 16 - 3Sum Closest

[leetcode link](https://leetcode.com/problems/3sum-closest/)

> Given an array `nums` of *n* integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.
>
> **Example 1:**
>
> ```
> Input: nums = [-1,2,1,-4], target = 1
> Output: 2
> Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
> ```
>
> **Constraints:**
>
> - `3 <= nums.length <= 10^3`
> - `-10^3 <= nums[i] <= 10^3`
> - `-10^4 <= target <= 10^4`

## Two pointers solution - O(n^2)

```cpp
// 12/09/2020
// two pointers 
int threeSumClosest(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int mindiff = numeric_limits<int>::max();
    int closest_sum;
    for(int i = 0, size = nums.size(); i != size-2; ++i){
        if(i>0 && nums[i] == nums[i-1]) continue;
        for(int j = i+1, k = size -1; j < k;){
            int sum = nums[i] + nums[j] + nums[k];
            int d = abs(sum - target);
            if(d == 0) return sum;
            if(d < mindiff){
                mindiff = d;
                closest_sum = sum;
            }
            if(sum > target)
                --k;
            else
                ++j;
        }
    }
    return closest_sum;
}
```