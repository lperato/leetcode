# 107 - Binary Tree Level Order Traversal II

[leetcode link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

> Given a binary tree, return the *bottom-up level order* traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
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
> return its bottom-up level order traversal as:
>
> ```
> [
>   [15,7],
>   [9,20],
>   [3]
> ]
> ```

## Recursive solution - DFS

```cpp
// 02/07/2020
vector<vector<int>> levelOrderBottom(TreeNode* root) {
    vector<vector<int>> result;
    level_order_dfs(root, result);
    reverse(result.begin(), result.end());
    return result;    
}

void level_order_dfs(vector<vector<int>>& levels, TreeNode* node, int n = 0){
    if(node==nullptr)return;
    if(levels.size() == n)
        levels.emplace_back(vector<int>(1, node->val));
    else
        levels[n].emplace_back(node->val);
    level_order_dfs(levels, node->left, n+1);
    level_order_dfs(levels, node->right, n+1); 
}
```
## Iterative solution - BFS

```cpp
// 02/07/2020
vector<vector<int>> levelOrderBottom(TreeNode* root){
    deque<vector<int>> result_dq;
    level_order_bottom_bfs(result_dq, root);
    vector<vector<int>> result;
    result.reserve(result_dq.size());
    move(result_dq.begin(), result_dq.end(), back_inserter(result));
    return move(result);
}

void level_order_bottom_bfs(deque<vector<int>>& levels, TreeNode* root){
    if(root == nullptr) return;
    queue<pair<TreeNode*, int>> queue;
    queue.emplace(root, 0);
    while(!queue.empty()){
        auto [node, level] = queue.front();
        if(levels.size()-level == 0) levels.emplace_front(1, node->val);
        else levels[levels.size()-level-1].emplace_back(node->val);
        queue.pop();
        if(node->left) queue.emplace(node->left, level+1);
        if(node->right) queue.emplace(node->right, level+1);
    }
}
```