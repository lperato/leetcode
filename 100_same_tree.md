# 100 - Same Tree

[leetcode link](https://leetcode.com/problems/same-tree/)

> Given two binary trees, write a function to check if they are the same or not.
>
> Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
>
> **Example 1:**
>
> ```
> Input:     1         1
>           / \       / \
>          2   3     2   3
> 
>         [1,2,3],   [1,2,3]
> 
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input:     1         1
>           /           \
>          2             2
> 
>         [1,2],     [1,null,2]
> 
> Output: false
> ```
>
> **Example 3:**
>
> ```
> Input:     1         1
>           / \       / \
>          2   1     1   2
> 
>         [1,2,1],   [1,1,2]
> 
> Output: false
> ```

## Recursive solutions

### Single statement as boolean expression

```cpp
// 13/07/2020
bool isSameTree(TreeNode* p, TreeNode* q) {
    return p!=nullptr && q!=nullptr 
        && p->val == q->val 
        && isSameTree(p->left, q->left) 
        && isSameTree(p->right, q->right)
        || p == q;
}
```
### Using conditional

```cpp
// 29/03/2020
bool isSameTree(TreeNode* p, TreeNode* q) {
    return p==nullptr?q==nullptr:(q==nullptr?false:(p->val==q->val 
        && isSameTree(p->left, q->left) 
        && isSameTree(p->right, q->right)));
}
```
## Iterative solution

```cpp
// 09/09/2020
bool isSameTree(TreeNode* p, TreeNode* q) {
    deque<pair<TreeNode*, TreeNode*>> queue;
    queue.emplace_back(p, q);
    while(!queue.empty()){
        for(int i = 0, size = queue.size(); i != size; ++i){
            auto [a, b] = queue.front();
            queue.pop_front();
            if((!a && b) ||(!b && a) || (a && b && a->val != b->val))
                return false;
            if(a){
                queue.emplace_back(a->left, b->left);
                queue.emplace_back(a->right, b->right);
            }
        }
    }
    return true;
}
```