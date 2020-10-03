# 145 - Binary Tree Postorder Traversal

[leetcode link](https://leetcode.com/problems/binary-tree-postorder-traversal/)

> Given the `root` of a binary tree, return *the postorder traversal of its nodes' values*.
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg)
>
> ```
> Input: root = [1,null,2,3]
> Output: [3,2,1]
> ```
>
> **Example 2:**
>
> ```
> Input: root = []
> Output: []
> ```
>
> **Example 3:**
>
> ```
> Input: root = [1]
> Output: [1]
> ```
>
> **Example 4:**
>
> ![img](https://assets.leetcode.com/uploads/2020/08/28/pre3.jpg)
>
> ```
> Input: root = [1,2]
> Output: [2,1]
> ```
>
> **Example 5:**
>
> ![img](https://assets.leetcode.com/uploads/2020/08/28/pre2.jpg)
>
> ```
> Input: root = [1,null,2]
> Output: [2,1]
> ```
>
> **Constraints:**
>
> - The number of the nodes in the tree is in the range `[0, 100]`.
> - `-100 <= Node.val <= 100`
>
> **Follow up:**
>
> Recursive solution is trivial, could you do it iteratively?

## Recursive solution

```cpp
// 15/09/2020
// recursive solution
vector<int> postorderTraversal(TreeNode* root) {
    vector<int> result;
    postorder_traversal_dfs(result, root);
    return result;
}

void postorder_traversal_dfs(vector<int>& result, const TreeNode *root){
    if(root == nullptr) return;
    postorder_traversal_dfs(result, root->left);
    postorder_traversal_dfs(result, root->right);
    result.push_back(root->val);
}
```
## Iterative solution

```cpp
// 15/09/2020
// iterative solution 1
vector<int> postorderTraversal(TreeNode* root) {
    if(root == nullptr) return {};
    vector<int> result;
    stack<TreeNode *> s1, s2;
    auto node = root;
    while(!s1.empty() || !s2.empty() || node){
        while(node){
            s1.push(node);
            node = node->left;
        }
        node = s1.top();
        s2.push(node);
        s1.pop();
        node = node->right;   
        if(s1.empty() && !node){
            while(!s2.empty()){
                result.push_back(s2.top()->val);
                s2.pop();
            }
        }
    }
    return result;
}
```