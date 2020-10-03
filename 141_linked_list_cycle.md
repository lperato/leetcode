# 141 - Linked List Cycle

[leetcode link](https://leetcode.com/problems/linked-list-cycle/)

> Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
>
> There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
>
> Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.
>
> **Follow up:**
>
> Can you solve it using `O(1)` (i.e. constant) memory?
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)
>
> ```
> Input: head = [3,2,0,-4], pos = 1
> Output: true
> Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
> ```
>
> **Example 2:**
>
> ![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)
>
> ```
> Input: head = [1,2], pos = 0
> Output: true
> Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
> ```
>
> **Example 3:**
>
> ![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)
>
> ```
> Input: head = [1], pos = -1
> Output: false
> Explanation: There is no cycle in the linked list.
> ```
>
> **Constraints:**
>
> - The number of the nodes in the list is in the range `[0, 104]`.
> - `-105 <= Node.val <= 105`
> - `pos` is `-1` or a **valid index** in the linked-list.

## Slow - fast pointer  solution

### Code golfing

```cpp
// 24/08/2020
bool hasCycle(ListNode* h){
    if(!h) return false;
    auto f = h->next;
    for(;h && f && f->next && f != h && f->next != h; h = h->next, f = f->next->next);
    return f && h && (f == h || f->next == h);
}
```
### Variant 1

```cpp
// 24/08/2020
bool hasCycle(ListNode* head){
    if(!head) return false;
    auto fast = head->next;
    while(fast && fast->next){
        if(fast == head || fast->next == head) 
            return true;
        fast = fast->next->next;
        head = head->next;
    }
    return false;
}
```
### Variant 2

```cpp
// 24/08/2020
bool hasCycle(ListNode* head){
    auto fast = head;
    while(fast && fast->next){
        fast = fast->next->next;
        head = head->next;
        if(fast && (fast == head || (head && fast->next == head)))
            return true;
    }
    return false;
}
```
### Variant 3

```cpp
// 16/03/2020
bool hasCycle(ListNode *head) {
    if (head == nullptr) return false;
    auto n1 = head;
    auto n2 = head->next;
    while(n1 != nullptr && n2 != nullptr){
        if(n2->next == n1 || n2 == n1)
            return true;
        n1 = n1->next;
        n2 = n2->next?n2->next->next:nullptr;
    }
    return false;
}
```