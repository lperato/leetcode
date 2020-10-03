# 143 - Reorder List

[leetcode link](https://leetcode.com/problems/reorder-list/)

> Given a singly linked list *L*: *L*0→*L*1→…→*L**n*-1→*L*n,
>  reorder it to: *L*0→*L**n*→*L*1→*L**n*-1→*L*2→*L**n*-2→…
>
> You may **not** modify the values in the list's nodes, only nodes itself may be changed.
>
> **Example 1:**
>
> ```
> Given 1->2->3->4, reorder it to 1->4->2->3.
> ```
>
> **Example 2:**
>
> ```
> Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
> ```

## find mid then interleave 2 lists

```cpp
// 27/08/2020
void reorderList(ListNode* head) {
    if(head == nullptr) return;
    auto mid = find_mid(head);
    auto tmp = mid->next;
    mid->next = nullptr;
    reorder_list(head, tmp);
}

ListNode *reorder_list(ListNode* l1, ListNode* l2){
    if(l2 == nullptr) return l1;
    auto tmp = reorder_list(l1, l2->next);
    l2->next = tmp->next;
    tmp->next = l2;
    return l2->next;
}

ListNode* find_mid(ListNode* head){
    for(auto fast = head; fast && fast->next; fast = fast->next->next)
        head = head->next;
    return head;
}
```