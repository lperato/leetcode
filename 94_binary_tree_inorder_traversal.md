# 94 - Binary Tree Inorder Traversal

[leetcode link](https://leetcode.com/problems/binary-tree-inorder-traversal/)

Given a binary tree, return the *inorder* traversal of its nodes' values.

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

**Follow up:** Recursive solution is trivial, could you do it iteratively?

## Recursive solution

```cpp
// 15/09/2020
// recursive solution
vector<int> inorderTraversal(TreeNode* root) {
    vector<int> result;
    inorder_traversal_dfs(root, result);
    return result;
}

void inorder_traversal_dfs(TreeNode* root, vector<int>& result){
    if(root == nullptr) return;
    inorder_traversal_dfs(root->left, result);
    result.push_back(root->val);
    inorder_traversal_dfs(root->right, result);
}
```
## Iterative solution 1

```cpp
// 15/09/2020
// iterative solution 1
vector<int> inorderTraversal(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> s;
    auto node = root;
    while(!s.empty() || node){
        while(node){
            s.push(node);
            node = node->left;
        }
        node = s.top();
        s.pop();
        result.push_back(node->val);
        node = node->right;
    }
    return result;
}
```
## Iterative solution 2

```cpp
// 15/09/2020
// iterative solution 2
vector<int> inorderTraversal(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> s;
    auto node = root;
    while(!s.empty() || node){
        if(node){
            s.push(node);
            node = node->left;
        } else {
            node = s.top();
            s.pop();
            result.push_back(node->val);
            node = node->right;
        }
    }
    return result;
}
```
