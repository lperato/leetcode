# 144 - Binary Tree Preorder Traversal

[leetcoded link](https://leetcode.com/problems/binary-tree-preorder-traversal/)

> Given a binary tree, return the *preorder* traversal of its nodes' values.
>
> **Example:**
>
> ```
> Input: [1,null,2,3]
>    1
>     \
>      2
>     /
>    3
> 
> Output: [1,2,3]
> ```
>
> **Follow up:** Recursive solution is trivial, could you do it iteratively?

## Recursive solution

```cpp
// 15/09/2020
// recursive solution
vector<int> preorderTraversal(TreeNode* root) {
    vector<int> result;
    preorder_traversal_dfs(result, root);
    return result;
}

void preorder_traversal_dfs(vector<int>& result, const TreeNode *root){
    if(root == nullptr) return;
    result.push_back(root->val);
    preorder_traversal_dfs(result, root->left);
    preorder_traversal_dfs(result, root->right);
}
```
## Iterative solution 1

```cpp
// 15/09/2020
// iterative solution 1
vector<int> preorderTraversal(TreeNode* root) {
    vector<int> result;
    stack<TreeNode *> s;
    auto node = root;
    while(!s.empty() || node){
        while(node){
            s.push(node);
            result.push_back(node->val);
            node = node->left;
        }
        node = s.top();
        s.pop();
        node = node->right;
    }
    return result;   
}
```
## Iterative solution 2

```cpp
// 15/09/2020
// iterative solution 2 (slightly faster)
vector<int> preorderTraversal(TreeNode* root) {
    vector<int> result;
    stack<TreeNode *> s;
    auto node = root;
    while(!s.empty() || node){
        if(node){
            s.push(node);
            result.push_back(node->val);
            node = node->left;
        } else {
            node = s.top();
            s.pop();
            node = node->right;
        }
    }
    return result;   
}
```