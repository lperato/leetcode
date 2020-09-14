# 39 - Combination Sum

[leetcode link](https://leetcode.com/problems/combination-sum/)

> Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.
>
> The **same** repeated number may be chosen from `candidates` unlimited number of times.
>
> **Note:**
>
> - All numbers (including `target`) will be positive integers.
> - The solution set must not contain duplicate combinations.
>
> **Example 1:**
>
> ```
> Input: candidates = [2,3,6,7], target = 7,
> A solution set is:
> [
>   [7],
>   [2,2,3]
> ]
> ```
>
> **Example 2:**
>
> ```
> Input: candidates = [2,3,5], target = 8,
> A solution set is:
> [
>   [2,2,2,2],
>   [2,3,3],
>   [3,5]
> ]
> ```
>
> **Constraints:**
>
> - `1 <= candidates.length <= 30`
> - `1 <= candidates[i] <= 200`
> - Each element of `candidate` is unique.
> - `1 <= target <= 500`

## Backtracking 

```cpp
vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    combination_sum_bt(candidates, result, comb, target);
    return result;
}

void combination_sum_bt(const vector<int>& candidates,  
                        vector<vector<int>>& result, vector<int>& comb, 
                        int target, int start=0){
    if(target <= 0){
        if(target == 0)
            result.push_back(comb);
        return;
    }
    for (int i=start, size=candidates.size(); i != size; ++i){
        comb.push_back(candidates[i]);
        combination_sum_bt(candidates, result, comb, target - candidates[i], i);
        comb.pop_back();
    }
}
```
