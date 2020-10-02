# 106 - Construct Binary Tree from Inorder and Postorder Traversal

[leetcode link](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

> Given inorder and postorder traversal of a tree, construct the binary tree.
>
> **Note:**
>  You may assume that duplicates do not exist in the tree.
>
> For example, given
>
> ```
> inorder = [9,3,15,20,7]
> postorder = [9,15,7,20,3]
> ```
>
> Return the following binary tree:
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```

## Recursive solution using iterators

```cpp
// 27/07/2020
TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
    return build_tree(inorder.begin(), inorder.end(), postorder.begin(), postorder.end());
}

using IT = vector<int>::const_iterator;

TreeNode *build_tree(IT io_begin, IT io_end, IT po_begin, IT po_end){
    if(io_begin == io_end) return nullptr;
    int rootval = *prev(po_end);
    auto io_root = find(io_begin, io_end, rootval);
    int leftsub_len = io_root-io_begin;
    return new TreeNode(
        rootval, 
        build_tree(io_begin, io_root, po_begin, po_begin + leftsub_len),
        build_tree(io_root+1, io_end,po_begin + leftsub_len, prev(po_end)));
}
```