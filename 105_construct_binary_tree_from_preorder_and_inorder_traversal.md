# 105 - Construct Binary Tree from Preorder and Inorder Traversal

[leetcode link](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

> Given preorder and inorder traversal of a tree, construct the binary tree.
>
> **Note:**
>  You may assume that duplicates do not exist in the tree.
>
> For example, given
>
> ```
> preorder = [3,9,20,15,7]
> inorder = [9,3,15,20,7]
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

## Recursive solution

### Using iterators

```cpp
// 08/03/2020
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    return build_node(preorder.begin(), preorder.end(),
                      inorder.begin(), inorder.end());
}

TreeNode* build_node(vector<int>::iterator pstart, 
                     vector<int>::iterator pend,
                     vector<int>::iterator istart,
                     vector<int>::iterator iend){
    if (pstart == pend || istart == iend)
        return NULL;
    auto pivot = istart;
    for (;pivot != iend && *pivot != *pstart; pivot++);
    if (pivot == pend)
        return NULL;
    auto node = new TreeNode(*pstart);
    node->left = build_node(pstart+1, pend, istart, pivot);     
    node->right = build_node(pstart + (pivot-istart)+1, pend, pivot+1, iend);
    return node;
}
```