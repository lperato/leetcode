# 40 - Combination Sum II

[leetcode link](https://leetcode.com/problems/combination-sum-ii/)

> Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.
>
> Each number in `candidates` may only be used **once** in the combination.
>
> **Note:**
>
> - All numbers (including `target`) will be positive integers.
> - The solution set must not contain duplicate combinations.
>
> **Example 1:**
>
> ```
> Input: candidates = [10,1,2,7,6,1,5], target = 8,
> A solution set is:
> [
>   [1, 7],
>   [1, 2, 5],
>   [2, 6],
>   [1, 1, 6]
> ]
> ```
>
> **Example 2:**
>
> ```
> Input: candidates = [2,5,2,1,2], target = 5,
> A solution set is:
> [
>   [1,2,2],
>   [5]
> ]
> ```

## Backtracking solution with initial sorting

```cpp
vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    sort(candidates.begin(), candidates.end());
    combination_sum_bt(candidates, result, comb, target);
    return result;
}

void combination_sum_bt(const vector<int>& candidates,  
                        vector<vector<int>>& result, vector<int>& comb, 
                        int target, int start=0){
    if(target <= 0 || start == candidates.size()){
        if(target == 0)
            result.push_back(comb);
        return;
    }
    for (int i=start, size=candidates.size(); i != size; ++i){
        if(i == start || candidates[i] != candidates[i-1]){
            comb.push_back(candidates[i]);
            combination_sum_bt(candidates, result, comb, target - candidates[i], i+1);
            comb.pop_back();
        }
    }
}
```