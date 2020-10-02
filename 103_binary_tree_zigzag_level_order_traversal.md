# 103 - Binary Tree Zigzag Level Order Traversal

[leetcode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

> Given a binary tree, return the *zigzag level order* traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
>
> For example:
>  Given binary tree `[3,9,20,null,null,15,7]`,
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> return its zigzag level order traversal as:
>
> ```
> [
>   [3],
>   [20,9],
>   [15,7]
> ]
> ```

## BFS solution

```cpp
22/07/2020
vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    if(root == nullptr) return {};
    deque<TreeNode*> nodes;
    nodes.push_back(root);
    vector<vector<int>> result;
    bool revert = false;
    while(!nodes.empty()){
        auto size = nodes.size();
        result.emplace_back(size);
        auto &level = result.back();
        for(int i = 0; i < size; ++i){
            auto n = nodes.front();
            nodes.pop_front();
            level[revert?size-i-1:i] = n->val;
            if(n->left) nodes.push_back(n->left);
            if(n->right) nodes.push_back(n->right);
        }
        revert = !revert;
    }
    return result;
}
```