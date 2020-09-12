# 82 - Remove Duplicates from Sorted List II

[leetcode link](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

> Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only *distinct* numbers from the original list.
>
> Return the linked list sorted as well.
>
> **Example 1:**
>
> ```
> Input: 1->2->3->3->4->4->5
> Output: 1->2->5
> ```
>
> **Example 2:**
>
> ```
> Input: 1->1->1->2->3
> Output: 2->3
> ```

## Iterative solution

**TODO** implement recursive solution

```cpp
ListNode* deleteDuplicates(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* newhead = nullptr;
    auto node = head;
    while(node){
        auto skip = node;
        while(skip->next && skip->val == skip->next->val){
            skip = skip->next;
        }
        if (skip != node){
            if (prev){
                prev->next = skip->next;
            }
            node = skip->next;
        }
        else{
            if (not newhead)
                newhead=node;
            prev = node;
            node = node->next;
        }
    }
    return newhead;
}
```