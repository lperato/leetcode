# 112 - Path Sum

[leetcode link](https://leetcode.com/problems/path-sum/)

> Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
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
>  /  \      \
> 7    2      1
> ```
>
> return true, as there exist a root-to-leaf path `5->4->11->2` which sum is 22.

## Recursive solution

```cpp
// 23/05/2020
bool hasPathSum(TreeNode* root, int sum, int s=0) {
    if (root == nullptr) return false;
    if(!root->left&& !root->right && s + root->val == sum)
        return true;
    if (hasPathSum(root->left, sum , s + root->val))
        return true;
    return hasPathSum(root->right, sum, s + root->val);
}
```