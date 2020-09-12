# 216 - Combination Sum III

[leetcode link](https://leetcode.com/problems/combination-sum-iii/)

> Find all possible combinations of ***k*** numbers that add up to a number ***n***, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
>
> **Note:**
>
> - All numbers will be positive integers.
> - The solution set must not contain duplicate combinations.
>
> **Example 1:**
>
> ```
> Input: k = 3, n = 7
> Output: [[1,2,4]]
> ```
>
> **Example 2:**
>
> ```
> Input: k = 3, n = 9
> Output: [[1,2,6], [1,3,5], [2,3,4]]
> ```

## Backtracking solution

```cpp
// 12/09/2020
vector<vector<int>> combinationSum3(int k, int n) {
    vector<vector<int>> result;
    vector<int> comb;
    combination_sum_3_bt(result, comb, k, n);
    return result;
}
void combination_sum_3_bt(vector<vector<int>>& result, vector<int>& comb, int k, int n){
    if(k == 0){
        if(n==0)
        	result.push_back(comb);
        return;
    }
    for(int i = comb.empty()?1:comb.back()+1; i != 10 && i <= n; ++i){
        comb.push_back(i);
        combination_sum_3_bt(result, comb, k-1, n-i);
        comb.pop_back();
    }
}
```