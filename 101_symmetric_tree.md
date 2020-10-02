# 101 - Symmetric Tree

[leetcode link](https://leetcode.com/problems/symmetric-tree/)

> Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
>
> For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:
>
> ```
>     1
>    / \
>   2   2
>  / \ / \
> 3  4 4  3
> ```
>
> But the following `[1,2,2,null,3,null,3]` is not:
>
> ```
>     1
>    / \
>   2   2
>    \   \
>    3    3
> ```
>
> **Follow up:** Solve it both recursively and iteratively.

## Recursive solution

```cpp
// 06/03/2020
bool isSymmetric(TreeNode* root) {
    if(root == NULL)
        return true;
    return is_symmetric(root->left, root->right);
}

bool is_symmetric(TreeNode* n1, TreeNode* n2){
    if (n1 == NULL && n2 == NULL)
        return true;
    if ((n1 == NULL && n2 != NULL) || (n1 != NULL && n2 == NULL))
        return false;
    if (n1->val != n2->val)
        return false;
    return is_symmetric(n1->left, n2->right) and is_symmetric(n1->right, n2->left);
}
```