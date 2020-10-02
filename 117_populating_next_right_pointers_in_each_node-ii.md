# 117 - Populating Next Right Pointers in Each Node II

[leetcode link](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

> Given a binary tree
>
> ```
> struct Node {
>   int val;
>   Node *left;
>   Node *right;
>   Node *next;
> }
> ```
>
> Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.
>
> Initially, all next pointers are set to `NULL`.
>
> **Follow up:**
>
> - You may only use constant extra space.
> - Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)
>
> ```
> Input: root = [1,2,3,4,5,null,7]
> Output: [1,#,2,3,#,4,5,7,#]
> Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
> ```
>
> **Constraints:**
>
> - The number of nodes in the given tree is less than `6000`.
> - `-100 <= node.val <= 100`

## BFS

```cpp
// 01/08/2020
Node* connect(Node* root) {
    if(root == nullptr) return nullptr;
    deque<Node*> queue{root};
    while(!queue.empty()){
        Node * prev = nullptr;
        for(int i = 0, size = queue.size(); i != size; ++i){
            Node *node = queue.front();
            queue.pop_front();
            if(prev) prev->next = node;
            if(node->left) queue.push_back(node->left);
            if(node->right) queue.push_back(node->right);
            prev = node;
        }
    }
    return root;
}
```