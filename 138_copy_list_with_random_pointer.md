# 138 - Copy List with Random Pointer

[leetcode link](https://leetcode.com/problems/copy-list-with-random-pointer/)

> A linked list  is given such that each node contains an additional random pointer which could point to any node in the list or null.
>
> Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list.
>
> The Linked List is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:
>
> - `val`: an integer representing `Node.val`
> - `random_index`: the index of the node (range from `0` to `n-1`) where random pointer points to, or `null` if it does not point to any node.
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2019/12/18/e1.png)
>
> ```
> Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
> Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
> ```
>
> **Example 2:**
>
> ![img](https://assets.leetcode.com/uploads/2019/12/18/e2.png)
>
> ```
> Input: head = [[1,1],[2,1]]
> Output: [[1,1],[2,1]]
> ```
>
> **Example 3:**
>
> **![img](https://assets.leetcode.com/uploads/2019/12/18/e3.png)**
>
> ```
> Input: head = [[3,null],[3,0],[3,null]]
> Output: [[3,null],[3,0],[3,null]]
> ```
>
> **Example 4:**
>
> ```
> Input: head = []
> Output: []
> Explanation: Given linked list is empty (null pointer), so return null. 
> ```
>
> **Constraints:**
>
> - `-10000 <= Node.val <= 10000`
> - `Node.random` is null or pointing to a node in the linked list.
> - Number of Nodes will not exceed 1000.

## Solution

```cpp
Node* copyRandomList(Node* head) {
    if(head == nullptr) return nullptr;
    unordered_map<Node*, Node*> node_copy;
    auto head_cp = new Node(head->val);
    head_cp->random = head->random;
    node_copy.emplace(head, head_cp);
    for(auto node_cp = head_cp, node = head->next; node != nullptr; node = node->next){
        node_cp->next = new Node(node->val);
        node_cp = node_cp->next;
        node_cp->random = node->random;
        node_copy.emplace(node, node_cp);
    }
    for(auto node_cp = head_cp; node_cp != nullptr; node_cp = node_cp->next)
        if(node_cp->random)
            node_cp->random = node_copy[node_cp->random];
    return head_cp;
}
```