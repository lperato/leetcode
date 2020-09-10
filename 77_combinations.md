# 77 - Combinations

[leetcode link](https://leetcode.com/problems/combinations/)

> Given two integers *n* and *k*, return all possible combinations of *k* numbers out of 1 ... *n*.
>
> You may return the answer in **any order**.
>
> **Example 1:**
>
> ```
> Input: n = 4, k = 2
> Output:
> [
>   [2,4],
>   [3,4],
>   [2,3],
>   [1,2],
>   [1,3],
>   [1,4],
> ]
> ```
>
> **Example 2:**
>
> ```
> Input: n = 1, k = 1
> Output: [[1]]
> ```
>
> **Constraints:**
>
> - `1 <= n <= 20`
> - `1 <= k <= n`

## Backtracking solution

```cpp
// 09/09/2020
vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> result;
    vector<int> comb(k);
    combine_bt(result, comb, n);
    return result;
}

void combine_bt(vector<vector<int>>& result, vector<int>& comb, int n, int k = 0){
    if(k==comb.size()){
        result.push_back(comb);
        return;
    }
    for(int i = n; i > 0; --i){
        comb[k] = i;
        combine_bt(result, comb, i-1, k+1);
    }
}
```