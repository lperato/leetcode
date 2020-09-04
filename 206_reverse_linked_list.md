# 206 - Reverse Linked List

[leetcode link](https://leetcode.com/problems/reverse-linked-list/)

## Recursive solution

```cpp
ListNode* reverseList(ListNode* head){
    if(!head) return nullptr;
    if(!head->next) return head;
    auto new_head = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return new_head;
}
```

## Iterative solution

```cpp
ListNode* reverseList(ListNode* head) {
    auto current = head;
    ListNode* new_head = NULL;
    while (current!= NULL){
        auto next = current->next;
        current->next = new_head;
        new_head = current;
        current = next;
    }
    return new_head;
}
```

