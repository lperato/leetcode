# 78 - Subsets

[leetcode link](https://leetcode.com/problems/subsets/)

> Given a set of **distinct** integers, *nums*, return all possible subsets (the power set).
>
> **Note:** The solution set must not contain duplicate subsets.
>
> **Example:**
>
> ```
> Input: nums = [1,2,3]
> Output:
> [
>   [3],
>   [1],
>   [2],
>   [1,2,3],
>   [1,3],
>   [2,3],
>   [1,2],
>   []
> ]
> ```

**TODO** re-solve that problem with proper backtracking solution 

## Backtracking-ish solution

```cpp
// 25/07/2020
vector<vector<int>> subsets(vector<int>& nums) {
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
        subset.resize(ssize+1); //subset.push_back(-1);
        for(int i = start; i<size; ++i){
            subset.back() = nums[i];
            generate_subsets(nums, result, subset, i+1);
        }
        subset.pop_back();
    }
}
```
## Backtracking-ish solution  (with pass by copy)

```cpp
// 11/07/2020
vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        result.reserve(1<<nums.size()); 
        generate_subsets(nums, result);
        return result;
    }
    
    void generate_subsets(const vector<int>& nums, vector<vector<int>>& result, 
                          vector<int> subset = {}, int start = 0){
        result.emplace_back(subset);
        if(auto ssize = subset.size(), size = nums.size(); ssize<size){
            subset.resize(ssize+1); //subset.push_back(-1);
            for(int i = start; i<size; ++i){
                subset.back() = nums[i];
                generate_subsets(nums, result, subset, i+1);
            }  
        }
    }
```
## Initial solution (weirder)

```cpp
// 11/07/2020
vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> result;
    for(int len = 0; len < nums.size()+1; ++len)
        generate_subsets(nums, result, len);
    return result;
}

void generate_subsets(const vector<int>& nums, vector<vector<int>>& result, int len, 
                      vector<int> subset = {}, int start = 0){
    
    if(auto ssize = subset.size(); ssize == len)
        result.emplace_back(subset);
    else if(ssize<len){
        subset.push_back(-1);
        int size = nums.size(); 
        for(int i = start; i<size; ++i){
            subset.back() = nums[i];
            generate_subsets(nums, result, len, subset, i+1);
        }  
    }
}
```