# 113 - Path Sum II

[leetcode link](https://leetcode.com/problems/path-sum-ii/)

> Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
>
> **Note:** A leaf is a node with no children.
>
> **Example:**
>
> Given the below binary tree and `sum = 22`,
>
> ```
>       5
>      / \
>     4   8
>    /   / \
>   11  13  4
>  /  \    / \
> 7    2  5   1
> ```
>
> Return:
>
> ```
> [
>    [5,4,11,2],
>    [5,8,4,5]
> ]
> ```

## Recursion + stack  / back tracking

```cpp
vector<vector<int>> pathSum(TreeNode* root, int sum) {
    vector<vector<int>> result;
    vector<int> path;
    path_sum(result, root, sum, path);
    return result;
}

void path_sum(vector<vector<int>>& allpaths, const TreeNode* root, int sum, vector<int>& path){
    if(root == nullptr) return;
    path.emplace_back(root->val);
    if(root->val == sum && !root->left && !root->right)
        allpaths.emplace_back(path);
    path_sum(allpaths, root->left, sum-root->val, path);
    path_sum(allpaths, root->right, sum-root->val, path);
    path.pop_back();
}
```