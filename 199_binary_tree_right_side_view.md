# 199 - Binary Tree Right Side View

[leetcode lnk](https://leetcode.com/problems/binary-tree-right-side-view/)

> Given a binary tree, imagine yourself standing on the *right* side of it, return the values of the nodes you can see ordered from top to bottom.
>
> **Example:**
>
> ```
> Input: [1,2,3,null,5,null,4]
> Output: [1, 3, 4]
> Explanation:
> 
>    1            <---
>  /   \
> 2     3         <---
>  \     \
>   5     4       <---
> ```

## Recursive solution (DFS):

```cpp
// 08/10/2020
vector<int> rightSideView(TreeNode* root) {
    vector<int> view;
    right_side_view_dfs(view, root);
    return view;
}

void right_side_view_dfs(vector<int>& view, TreeNode *root, int depth=0){
    if(root != nullptr){
        if(depth == view.size())
            view.push_back(root->val);
        else
            view[depth] = root->val;
        right_side_view_dfs(view, root->left, depth+1);
        right_side_view_dfs(view, root->right, depth+1);
    }
}
```
## Iterative solution (BFS)

```cpp
// 08/10/2020
vector<int> rightSideView(TreeNode* root) {
    vector<int> view;
    if(root){
        deque<TreeNode*> queue;
        queue.push_back(root);
        while(!queue.empty()){
            view.push_back(queue.back()->val);
            for(int i =0, size=queue.size(); i != size; ++i){
                auto node = queue.front();
                queue.pop_front();
                if(node->left)
                    queue.push_back(node->left);
                if(node->right)
                    queue.push_back(node->right);
            }
        }
    }
    return view;
}
```