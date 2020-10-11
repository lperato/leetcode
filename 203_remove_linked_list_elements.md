# 203 - Remove Linked List Elements

[leetcode link](https://leetcode.com/problems/remove-linked-list-elements/)

> Remove all elements from a linked list of integers that have value ***val\***.
>
> **Example:**
>
> ```
> Input:  1->2->6->3->4->5->6, val = 6
> Output: 1->2->3->4->5
> ```

## Recursive solution

```cpp
// 05/07/2020
ListNode* removeElements(ListNode* head, int val) {
    if(head == nullptr) return nullptr;
    if(head->val == val){
        auto tmp = head->next;
        delete head;
        head = tmp;
        return removeElements(head, val);
    }
    head->next = removeElements(head->next, val);
    return head;
}
```
## Iterative solution

```cpp
// 05/07/2020
ListNode* removeElements(ListNode* head, int val) {
    ListNode* prev = nullptr;
    ListNode* node = head;
    while(node!=nullptr){
        if(node->val == val){
            if(prev == nullptr){
                head = node->next;
                delete node;
                node = head;
            }else{
                prev->next = node->next;
                delete node;
                node = prev->next;
            }
        }else{
            prev = node;
            node = node->next;
        }
    }
    return head;
}
```