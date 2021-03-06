# 147 - Insertion Sort List

[leetcode link](https://leetcode.com/problems/insertion-sort-list/)

> Sort a linked list using insertion sort.
>
> ![img](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)
>  A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
>  With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
>
> **Algorithm of Insertion Sort:**
>
> 1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
> 2. At each iteration, insertion sort removes one element from the  input data, finds the location it belongs within the sorted list, and  inserts it there.
> 3. It repeats until no input elements remain.
>
> **Example 1:**
>
> ```
> Input: 4->2->1->3
> Output: 1->2->3->4
> ```
>
> **Example 2:**
>
> ```
> Input: -1->5->3->4->0
> Output: -1->0->3->4->5
> ```

## Solution

```cpp
ListNode* insertionSortList(ListNode* head) {
    if(head==nullptr || head->next==nullptr)
        return head;
    auto node = head->next;
    head->next=nullptr;
    auto newhead = head; 
    while(node){
        auto next = node->next;
        node->next = nullptr;
        newhead = insert_sorted(newhead, node); 
        node = next;
    }
    return newhead;
}

ListNode* insert_sorted(ListNode* head, ListNode* new_node){
    ListNode *prev = nullptr;
    auto node = head;
    int n = 0;
    while(node && node->val < new_node->val){
        prev = node;
        node = node->next;
    }
    new_node->next = node;
    if (prev){
        prev->next = new_node;
        return head;
    }
    return new_node;
}  
```