# 110 - Balanced Binary Tree

[leetcode link](https://leetcode.com/problems/balanced-binary-tree/)

> Given a binary tree, determine if it is height-balanced.
>
> For this problem, a height-balanced binary tree is defined as:
>
> > a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1.
>
> **Example 1:**
>
> Given the following tree `[3,9,20,null,null,15,7]`:
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> Return true.
>  
>  **Example 2:**
>
> Given the following tree `[1,2,2,3,3,null,null,4,4]`:
>
> ```
>        1
>       / \
>      2   2
>     / \
>    3   3
>   / \
>  4   4
> ```
>
> Return false.

## Recursive solution

```cpp
// 16/04/2020
bool isBalanced(TreeNode* root) {
    return is_balanced(root).first;
}

pair<bool, int> is_balanced(TreeNode* root){
    if(root == nullptr){
        return pair<bool, int>{true, 0};
    }
    auto left = is_balanced(root->left);
    auto right = is_balanced(root->right);
    return pair<bool, int>{
        left.first && right.first && abs(left.second-right.second) < 2,
        1+ max(left.second, right.second)};
}
```