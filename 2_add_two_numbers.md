# 2 - Add Two Numbers

[leetcode link](https://leetcode.com/problems/add-two-numbers/)

>You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
>
>You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Recursive solution

```cpp
// 01/09/2020
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2, bool carry=false) {
    if(!l1 && !l2) return carry?new ListNode(1):nullptr;
    int val = (l1?l1->val:0) + (l2?l2->val:0) + carry;
    carry = val >= 10;
    auto node = new ListNode(val%10);
    node->next = addTwoNumbers(l1?l1->next:nullptr, l2?l2->next:nullptr, carry);
    return node;
}
```

## Iterative solution (ugly version)

**TODO** rework that version

```cpp
// 25/02/2020
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int carry = 0;
    ListNode* head = NULL;
    ListNode* node = NULL;
    ListNode* last = NULL;
    ListNode* p1 = l1;
    ListNode* p2 = l2;
    while(p1!=NULL || p2 != NULL || carry == 1){
        int val = (p1?p1->val:0) + (p2?p2->val:0) + carry;
        node = new ListNode(val%10);
        if(!head)
            head = node;
        if(last)
            last->next = node;
        last = node;
        
        if (val>9)
            carry = 1;
        else
            carry = 0;

        if(p1)
            p1=p1->next;
        if(p2)
            p2=p2->next; 
    }
    return head;
}
```
