# 104 - Maximum Depth of Binary Tree

[leetcode link](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

>Given a binary tree, find its maximum depth.

> The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

>  **Note:** A leaf is a node with no children.

## Recursive solution 1

```cpp
int maxDepth(TreeNode* root) {
    return root?1 + max(maxDepth(root->left), maxDepth(root->right)):0;
}
```
## Recursive solution 2

```cpp
// pseudo tail recursion
int maxDepth(TreeNode *root){
    int maxdepth = 0;
    max_depth(root, maxdepth);
    return maxdepth;
}

void max_depth(TreeNode *root, int& maxdepth, int depth = 1){
    if(!root) return;
    maxdepth = max(maxdepth, depth);
    max_depth(root->left, maxdepth, depth+1);
    max_depth(root->right, maxdepth, depth+1);
}
```