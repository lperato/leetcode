# 102 - Binary Tree Level Order Traversal

[leetcode link](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

For example:
 Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```

## Recursive solution - DFS

```cpp
// 03/04/2020
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    level_order_dfs(result, root);
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
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    level_order_bfs(result, root);
    return result;
}

void level_order_bfs(vector<vector<int>>& levels, TreeNode* root){
    if(root == nullptr) return;
    queue<pair<TreeNode*, int>> queue;
    queue.push({root, 0});
    while(!queue.empty()){
        auto [node, level] = queue.front();
        if(level==levels.size()) levels.emplace_back(1, node->val);
        else levels[level].emplace_back(node->val);
        queue.pop();
        if(node->left) queue.push({node->left, level+1});
        if(node->right) queue.push({node->right, level+1});
    }
}
```