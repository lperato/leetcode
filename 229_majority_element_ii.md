# 229 - Majority Element II

[leetcode link](https://leetcode.com/problems/majority-element-ii/)

> Given an integer array of size *n*, find all elements that appear more than `⌊ n/3 ⌋` times.
>
> **Note:** The algorithm should run in linear time and in O(1) space.
>
> **Example 1:**
>
> ```
> Input: [3,2,3]
> Output: [3]
> ```
>
> **Example 2:**
>
> ```
> Input: [1,1,1,3,3,2,2,2]
> Output: [1,2]
> ```

## Solution using Boyer Moore Vote Algorithm

[Boyer–Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)

```cpp
// 22/09/2020
vector<int> majorityElement(vector<int>& nums) {
    if(nums.size() < 2) return nums;
    int e1, e2;
    for(int i=0, size=nums.size(), c1=0, c2=0; i != size; ++i){
        if(c1 == 0 && (i == 0 || nums[i] != e2)) 
            e1 = nums[i];
        if(c2 == 0 && nums[i] != e1)
            e2 = nums[i];
        if(nums[i] == e1)
            ++c1;
        else if(nums[i] == e2)
            ++c2;
        else{
            --c1;
            --c2;
        }
    }
    vector<int> result;
    int n1 = count(nums.begin(), nums.end(), e1);
    if(n1 > nums.size()/3)
        result.push_back(e1);
    int n2 = count(nums.begin(), nums.end(), e2);
    if(n2 > nums.size()/3 && e2 != e1)
        result.push_back(e2);
    return result;
}
```