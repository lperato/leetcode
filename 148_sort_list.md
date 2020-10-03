# 148 - Sort List

[leetcode link](https://leetcode.com/problems/sort-list/)

> Given the `head` of a linked list, return *the list after sorting it in **ascending order***.
>
> **Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)
>
> ```
> Input: head = [4,2,1,3]
> Output: [1,2,3,4]
> ```
>
> **Example 2:**
>
> ![img](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)
>
> ```
> Input: head = [-1,5,3,4,0]
> Output: [-1,0,3,4,5]
> ```
>
> **Example 3:**
>
> ```
> Input: head = []
> Output: []
> ```
>
> **Constraints:**
>
> - The number of nodes in the list is in the range `[0, 5 * 104]`.
> - `-105 <= Node.val <= 105`

## Solution 1 : insertion sort - O(n^2) - TLE

```cpp
// 14/08/2020
// insertion sort solution : TLE
ListNode* sortList(ListNode* head) {
    if(head==nullptr) return nullptr;
    head->next = sortList(head->next);
    return insert_sorted(head->next, head);
}

ListNode* insert_sorted(ListNode*head, ListNode *node){
    if(head == nullptr || node->val < head->val)
        return node;
    node->next = head->next;
    head->next = insert_sorted(head->next, node);
    return head;
}
```
## Solution 2: merge sort - O(n log(n))

```cpp
// 14/08/2020
// merge sort (divide, sort, merge)
ListNode* sortList(ListNode* head) {    
    if(head == nullptr || head->next == nullptr) return head; 
    auto prev_mid = find_prev_midpoint(head);
    auto mid = prev_mid->next;
    prev_mid->next = nullptr;
    auto head1 = sortList(head);
    auto head2 = sortList(mid);
    return merge_sorted(head1, head2);
}

ListNode* merge_sorted(ListNode* l1, ListNode* l2) {
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

ListNode* find_prev_midpoint(ListNode *head){
    auto fast = head;
    auto prev = head;
    while(fast && fast->next){
        prev = head;
        head = head->next;
        fast = fast->next->next;
    }
    return prev;
}
```