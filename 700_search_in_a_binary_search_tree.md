# 700 - Search in a Binary Search Tree

[leetcode link](https://leetcode.com/problems/search-in-a-binary-search-tree/)

> Given the root node of a binary search tree (BST) and a value. You need  to find the node in the BST that the node's value equals the given  value. Return the subtree rooted with that node. If such node doesn't  exist, you should return NULL.
>
> ...
>
> Note that an empty tree is represented by `NULL`, therefore you would see the expected output (serialized tree format) as `[]`, not `null`.

## Recursive solution

```cpp
// recursive version
TreeNode* searchBST(TreeNode* root, int val) {
    if (root ==nullptr) return nullptr;
    if (root->val == val) return root;
    return val < root->val?searchBST(root->left, val):searchBST(root->right, val); 
}
```
## Iterative solution

```cpp
// iterative
TreeNode* searchBST(TreeNode* root, int val) {
    while(root != nullptr && root->val != val)
        root=val < root->val?root->left:root->right;
    return root;
}
```
