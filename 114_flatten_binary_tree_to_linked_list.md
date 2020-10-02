# 114 - Flatten Binary Tree to Linked List

[leetcode link](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

## Recursive solution

```cpp
// 15/04/2020
void flatten(TreeNode* root) {
    if(root)
        _flatten(root);
}

TreeNode * _flatten(TreeNode *root){
    auto last = root;
    auto left = root->left;
    auto right = root->right;
    if(left){
        last->right = left;
        last = _flatten(left);
        root->left = nullptr;
    }
    if(right){
        last->right = right;
        last = _flatten(right);
    }
    return last;
}
```