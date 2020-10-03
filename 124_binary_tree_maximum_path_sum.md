# 124 - Binary Tree Maximum Path Sum

[leetcode link](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

> Given a **non-empty** binary tree, find the maximum path sum.
>
> For this problem, a path is defined as any sequence of nodes from  some starting node to any node in the tree along the parent-child  connections. The path must contain **at least one node** and does not need to go through the root.
>
> **Example 1:**
>
> ```
> Input: [1,2,3]
> 
>        1
>       / \
>      2   3
> 
> Output: 6
> ```
>
> **Example 2:**
>
> ```
> Input: [-10,9,20,null,null,15,7]
> 
>    -10
>    / \
>   9  20
>     /  \
>    15   7
> 
> Output: 42
> ```

## Solution

```cpp
// 29/04/2020
int maxPathSum(TreeNode* root) {
    int result = numeric_limits<int>::min();
    max_branch(root, result);
    return result;
}
int max_branch(TreeNode* root, int& max_path){
    if(root==nullptr)return 0;
    int left = max_branch(root->left, max_path);
    int right = max_branch(root->right, max_path);
    int maxbranch = max(root->val, root->val + max(left, right));
    max_path = max({max_path, 
                    maxbranch,
                    root->val+left+right,});
    return maxbranch;
}
```