# 90 - Subsets II

[leetcode link](https://leetcode.com/problems/subsets-ii/)

> Given a collection of integers that might contain duplicates, ***nums\***, return all possible subsets (the power set).
>
> **Note:** The solution set must not contain duplicate subsets.
>
> **Example:**
>
> ```
> Input: [1,2,2]
> Output:
> [
>   [2],
>   [1],
>   [1,2,2],
>   [2,2],
>   [1,2],
>   []
> ]
> ```

## Backtracking like solution

```cpp
// 25/07/2020
vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    result.reserve(1<<nums.size()); 
    vector<int> subset;
    generate_subsets(nums, result, subset);
    return result;
}

void generate_subsets(const vector<int>& nums, vector<vector<int>>& result, 
                      vector<int>& subset, int start = 0){
    result.emplace_back(subset);
    if(auto ssize = subset.size(), size = nums.size(); ssize<size){
        subset.resize(ssize+1); 
        for(int i = start; i<size; ++i){
            if(i == start || nums[i] != nums[i-1]){
                subset.back() = nums[i];
                generate_subsets(nums, result, subset, i+1);
            }
        }
        subset.pop_back();
    }
}
```
