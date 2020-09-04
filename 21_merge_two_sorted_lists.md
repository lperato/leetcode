# 21 - Merge Two Sorted Lists

[leetcode link](https://leetcode.com/problems/merge-two-sorted-lists/)

> Merge two sorted linked lists and return it as a new **sorted** list. The new list should be made by splicing together the nodes of the first two lists.

## Recursive solution

```cpp
// 01/09/2020
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if(l1 == nullptr) return l2;
    if(l2 == nullptr) return l1;
    if(l1->val < l2->val){
        l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    }else {
        l2->next = mergeTwoLists(l1, l2->next);
        return l2;
    }
}
```
## Iterative solution

```cpp
// 14/08/2020
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if(l1 == nullptr) return l2;
    if(l2 == nullptr) return l1;
    auto head = l1->val < l2->val?l1:l2;
    auto node = head;
    if(node == l1)
        l1 = l1->next;
    else
        l2 = l2->next;
    while(l1 != nullptr && l2 != nullptr){
        if(l1->val < l2->val){
            node->next = l1;
            l1 = l1->next;
        } else {
            node->next = l2;
            l2 = l2->next;
        }
        node = node->next;
        node->next = nullptr;
    }
    node->next = l1?l1:l2;
    return head;
}
```
## Ugly iterative solution

```cpp
// 24/02/2020
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode* n1 = l1;
    ListNode* n2 = l2;
    ListNode* head = NULL;
    ListNode* curr = NULL;
    while(n1!=NULL && n2 != NULL){
        if(head == NULL){
            if (n1->val <= n2->val){
                head = n1;
                n1 = n1->next;
            }
            else{
                head = n2;
                n2 = n2->next;
            }
            curr = head;
            curr->next = NULL;
        }
        else{
            if(n1->val <= n2->val){
                curr->next = n1;
                n1 = n1->next;
            }
            else{
                curr->next = n2;
                n2 = n2->next;
            }
            curr = curr->next;
            curr->next = NULL;
        }
    }
    if (head == NULL)
        return n1 != NULL ? n1 : n2;
    if (n1!=NULL)
        curr->next = n1;
    else if(n2!=NULL) 
        curr->next = n2;
    return head;
}
```