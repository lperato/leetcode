# 61 - Rotate List

[leetcode link](https://leetcode.com/problems/rotate-list/)

> Given a linked list, rotate the list to the right by *k* places, where *k* is non-negative.
>
> **Example 1:**
>
> ```
> Input: 1->2->3->4->5->NULL, k = 2
> Output: 4->5->1->2->3->NULL
> Explanation:
> rotate 1 steps to the right: 5->1->2->3->4->NULL
> rotate 2 steps to the right: 4->5->1->2->3->NULL
> ```
>
> **Example 2:**
>
> ```
> Input: 0->1->2->NULL, k = 4
> Output: 2->0->1->NULL
> Explanation:
> rotate 1 steps to the right: 2->0->1->NULL
> rotate 2 steps to the right: 1->2->0->NULL
> rotate 3 steps to the right: 0->1->2->NULL
> rotate 4 steps to the right: 2->0->1->NULL
> ```

## Solution

```cpp
06/03/2020
ListNode* rotateRight(ListNode* head, int k) {
    if(head == NULL || head->next == NULL || k == 0)
        return head;
    auto last = head;
    int size = 1;
    while(last->next != NULL){
        size++;
        last = last->next;
    }
    int K = k%size;
    if (K == 0)
        return head;
    auto new_last = head;
    for(int i = 0; i < size-K-1; i++) new_last = new_last->next;
    auto new_head = new_last->next;
    last->next = head;
    new_last->next = NULL;
    return new_head;
}
```