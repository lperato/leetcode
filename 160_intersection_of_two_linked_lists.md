# 160 - Intersection of Two Linked Lists

[leetcode link](https://leetcode.com/problems/intersection-of-two-linked-lists/)

> Write a program to find the node at which the intersection of two singly linked lists begins.
>
> For example, the following two linked lists:
>
> [![img](https://assets.leetcode.com/uploads/2018/12/13/160_statement.png)](https://assets.leetcode.com/uploads/2018/12/13/160_statement.png)
>
> begin to intersect at node c1.
>
> **Example 1:**
>
> [![img](https://assets.leetcode.com/uploads/2020/06/29/160_example_1_1.png)](https://assets.leetcode.com/uploads/2020/06/29/160_example_1_1.png)
>
> ```
> Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
> Output: Reference of the node with value = 8
> Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
> ```
>
> **Example 2:**
>
> [![img](https://assets.leetcode.com/uploads/2020/06/29/160_example_2.png)](https://assets.leetcode.com/uploads/2020/06/29/160_example_2.png)
>
> ```
> Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
> Output: Reference of the node with value = 2
> Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
> ```
>
> **Example 3:**
>
> [![img](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)
>
> ```
> Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
> Output: null
> Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
> Explanation: The two lists do not intersect, so return null.
> ```
>
> **Notes:**
>
> - If the two linked lists have no intersection at all, return `null`.
> - The linked lists must retain their original structure after the function returns.
> - You may assume there are no cycles anywhere in the entire linked structure.
> - Each value on each linked list is in the range `[1, 10^9]`.
> - Your code should preferably run in O(n) time and use only O(1) memory.

## Solutions

```cpp
// 30/08/2020
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    int len_a = list_length_r(headA);
    int len_b = list_length_r(headB);
    auto node = len_a>len_b?headA:headB;
    for(int i = 0, n = abs(len_a - len_b); i !=n; ++i)
        node = node->next;
    for(auto n = len_a>len_b?headB:headA; n != node; n = n->next)
        node = node->next;
    return node;
}
    
int list_length_r(ListNode *root){
    return root?1+list_length_r(root->next):0;
}
```
### older solution

```cpp
// 16/03/2020
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    int s1 = 0;
    int s2 = 0;
    auto node = headA;
    while(node != nullptr){s1++; node=node->next;}
    node = headB;
    while(node != nullptr){s2++; node=node->next;}
    auto n1 = headA;
    auto n2 = headB;
    if(s1>s2){
        for(int i = 0; i < s1-s2; i++) n1=n1->next;
    } else {
        for(int i = 0; i < s2-s1; i++) n2=n2->next;
    }
    while(n1 != nullptr && n1 != n2){
        n1=n1->next;
        n2=n2->next;
    }
    return n1;
}
```