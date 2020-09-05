# 19 - Remove Nth Node From End of List

[leetcode link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/

> Given a linked list, remove the *n*-th node from the end of list and return its head.
>
> **Example:**
>
> ```
> Given linked list: 1->2->3->4->5, and n = 2.
> 
> After removing the second node from the end, the linked list becomes 1->2->3->5.
> ```
>
> **Note:**
>
> Given *n* will always be valid.
>
> **Follow up:**
>
> Could you do this in one pass?

**TODO** implement the one pass solution

## 2 passes recursive solution with delete

```cpp
// 29/08/2020 
// recrusive solution with delete
ListNode* removeNthFromEnd(ListNode* head, int n){
    if (head == nullptr) return nullptr;
    auto prev = nth_from_end(head, n+1).first;
    if(prev){
        auto to_remove = prev->next;
        prev->next = to_remove->next;
        delete to_remove;
        return head;
    }else{
        auto new_head = head->next;
        delete head;
        return new_head;
    }
}

pair<ListNode *, int> nth_from_end(ListNode* head, int n){
    if(head == nullptr) return {nullptr, 0};
    auto [p, pos] = nth_from_end(head->next, n);
    if(p) return {p, pos};
    else if(pos+1 == n) return {head, pos+1};
    else return {nullptr, pos+1};
}
```
## 2 passes iterative solution

```cpp
// 21/02/2020
ListNode* removeNthFromEnd(ListNode* head, int n) {
    auto node = head;
    int size = 0;
    while(node != NULL){
        node = node->next;
        size++;
    }
    return removeNth(head, size - n + 1);
}

ListNode* removeNth(ListNode* head, int n) {
    if(head->next == NULL)
        return NULL;
    ListNode* node = head;
    ListNode* prev = NULL;
    for(int i = 0; i < n-1; i++){
        prev = node;
        node = node->next;
    }
    if (node == head){
        auto tmp = node->next;
        node->next = NULL;
        return tmp;
    }else{
        prev->next = node->next;
    }
    return head;
}
```