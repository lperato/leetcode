# 98 - Validate Binary Search Tree

[leetcode link](https://leetcode.com/problems/validate-binary-search-tree/)

> Given a binary tree, determine if it is a valid binary search tree (BST).
>
> Assume a BST is defined as follows:
>
> - The left subtree of a node contains only nodes with keys **less than** the node's key.
> - The right subtree of a node contains only nodes with keys **greater than** the node's key.
> - Both the left and right subtrees must also be binary search trees.
>
> **Example 1:**
>
> ```
>     2
>    / \
>   1   3
> 
> Input: [2,1,3]
> Output: true
> ```
>
> **Example 2:**
>
> ```
>     5
>    / \
>   1   4
>      / \
>     3   6
> 
> Input: [5,1,4,null,null,3,6]
> Output: false
> Explanation: The root node's value is 5 but its right child's value is 4.
> ```

## Code Golfing using pointers

```cpp
// 06/09/2020
// Code golfed solution using pointers and short varaible names :-)
bool isValidBST(TreeNode* n, int* lo=nullptr, int* hi=nullptr){ 
    return !n || ((!lo || n->val > *lo) && (!hi || n->val < *hi)
        && isValidBST(n->left, lo, &(n->val)) 
        && isValidBST(n->right, &(n->val), hi));
}
```
## Using optional values for min max filters

```cpp
// 20/08/2020
// solution using optional instead of int64_t - branchless
bool isValidBST(TreeNode* root, 
                optional<int> minval = nullopt, 
                optional<int> maxval = nullopt){ 
    return root == nullptr || (
           (!minval || root->val > minval.value()) 
        && (!maxval || root->val < maxval.value())
        && isValidBST(root->left, minval, root->val) 
        && isValidBST(root->right, root->val, maxval));
}
```
### initial version with multiple branches

```cpp
// 20/08/2020
// solution using optional instead of int64_t
bool isValidBST(TreeNode* root, 
                optional<int> minval = nullopt, 
                optional<int> maxval = nullopt){ 
    if(root == nullptr) return true;
    if((minval && root->val <= minval.value()) 
    || (maxval && root->val >= maxval.value())) return false;
    return isValidBST(root->left, minval, root->val) 
        && isValidBST(root->right, root->val, maxval);
}
```
## Using INT_MAX and INT_MIN :-(

```cpp
// 20/08/2020
bool isValidBST(TreeNode* root, 
                int64_t minv=numeric_limits<int64_t>::min(), 
                int64_t maxv=numeric_limits<int64_t>::max()){
    if(root == nullptr) return true;
    if(root->val <= minv || root->val >= maxv) return false;
    return isValidBST(root->left, minv, root->val) 
        && isValidBST(root->right, root->val, maxv);
}
```