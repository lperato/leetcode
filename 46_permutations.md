# 46 - Permutations

[leetcode link](https://leetcode.com/problems/permutations/)

> Given a collection of **distinct** integers, return all possible permutations.
>
> **Example:**
>
> ```
> Input: [1,2,3]
> Output:
> [
>   [1,2,3],
>   [1,3,2],
>   [2,1,3],
>   [2,3,1],
>   [3,1,2],
>   [3,2,1]
> ]
> ```

## Backtracking

```cpp
// 13/09/2020
vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> perm;
    vector<bool> used(nums.size());            
    permute_bt(nums, result, used, perm);
    return result;
}

void permute_bt(const vector<int>& nums, vector<vector<int>>& result, 
                vector<bool>& used, vector<int>&perm, int pos=0){
    if(pos == nums.size()){
        result.push_back(perm);
        return;
    }
    for(int i=0, size = nums.size(); i != size; ++i){
        if(!used[i]){
            used[i] = true;
            perm.push_back(nums[i]);
            permute_bt(nums, result, used, perm, pos+1);
            perm.pop_back();
            used[i] = false;
        }
    }
}
```