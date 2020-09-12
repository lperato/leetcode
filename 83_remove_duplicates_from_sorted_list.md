# 83 - Remove Duplicates from Sorted List

[leetcode link](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

> Given a sorted linked list, delete all duplicates such that each element appear only *once*.
>
> **Example 1:**
>
> ```
> Input: 1->1->2
> Output: 1->2
> ```
>
> **Example 2:**
>
> ```
> Input: 1->1->2->3->3
> Output: 1->2->3
> ```

## Solution

```cpp
ListNode* deleteDuplicates(ListNode* head) {
    auto node = head;
    while(node != nullptr){
        if(node->next && node->val == node->next->val){
            node->next = node->next->next;
        }            
        else
            node = node->next;
    }
    return head;    
}
```
**TODO** Implement recursive solution

