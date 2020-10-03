# 142 - Linked List Cycle II

[leetcode link](https://leetcode.com/problems/linked-list-cycle-ii/)

> Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.
>
> There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
>
> **Notice** that you **should not modify** the linked list.
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
> Output: tail connects to node index 1
> Explanation: There is a cycle in the linked list, where tail connects to the second node.
> ```
>
> **Example 2:**
>
> ![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)
>
> ```
> Input: head = [1,2], pos = 0
> Output: tail connects to node index 0
> Explanation: There is a cycle in the linked list, where tail connects to the first node.
> ```
>
> **Example 3:**
>
> ![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)
>
> ```
> Input: head = [1], pos = -1
> Output: no cycle
> Explanation: There is no cycle in the linked list.
> ```
>
> **Constraints:**
>
> - The number of the nodes in the list is in the range `[0, 104]`.
> - `-105 <= Node.val <= 105`
> - `pos` is `-1` or a **valid index** in the linked-list.

## Solution O(n) time - O(1) space

```cpp
ListNode *detectCycle(ListNode *head) {
    if(!head) return nullptr;
    auto n1=head;
    auto n2=head;
    do{
        n1 = n1->next;
        n2 = n2->next?n2->next->next:nullptr;
    } while(n2 && n1 != n2);
    if(!n2) return nullptr;
    n1=head;
    while(n1 != n2){
        n1 = n1->next;
        n2 = n2->next;
    }
    return n1;
}
```