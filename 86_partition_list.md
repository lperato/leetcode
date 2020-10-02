# 86 - Partition List

> Given a linked list and a value *x*, partition it such that all nodes less than *x* come before nodes greater than or equal to *x*.
>
> You should preserve the original relative order of the nodes in each of the two partitions.
>
> **Example:**
>
> ```
> Input: head = 1->4->3->2->5->2, x = 3
> Output: 1->2->2->4->3->5
> ```

**TODO** Implement iterative solution

## Recursive solution 

```cpp
// 28/09/2020
ListNode* partition(ListNode* head, int x) {
    if(head != nullptr){
        auto p = partition(head->next, x);
        if(head->val < x)
            head->next = p;
        else
            head = insert_after(p, head, x);
    }
    return head;
}

ListNode* insert_after(ListNode* head, ListNode *node, int x, ListNode* prev=nullptr){
    if(head == nullptr || head->val >= x){
        if(prev)
            prev->next = node;
        node->next = head;
        head = node;
    } else
        insert_after(head->next, node, x, head);
    return head;
}
```