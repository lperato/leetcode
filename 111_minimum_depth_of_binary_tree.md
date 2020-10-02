# 111 - Minimum Depth of Binary Tree

[leetcode link](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

> Given a binary tree, find its minimum depth.
>
> The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
>
> **Note:** A leaf is a node with no children.
>
> **Example:**
>
> Given binary tree `[3,9,20,null,null,15,7]`,
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> return its minimum depth = 2.

## Recursive solution

```cpp
// 16/04/2020
int minDepth(TreeNode* root) {
    if(root==nullptr){
        return 0;
    }
    return  1+((root->left && root->right)?
        min(minDepth(root->left), minDepth(root->right))
        :max(minDepth(root->left), minDepth(root->right)));
}
```