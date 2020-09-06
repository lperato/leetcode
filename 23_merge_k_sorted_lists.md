# 23 - Merge k Sorted Lists

[leetcode link](https://leetcode.com/problems/merge-k-sorted-lists/)

> You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.
>
> *Merge all the linked-lists into one sorted linked-list and return it.*
>
> **Example 1:**
>
> ```
> Input: lists = [[1,4,5],[1,3,4],[2,6]]
> Output: [1,1,2,3,4,4,5,6]
> Explanation: The linked-lists are:
> [
>   1->4->5,
>   1->3->4,
>   2->6
> ]
> merging them into one sorted list:
> 1->1->2->3->4->4->5->6
> ```
>
> **Example 2:**
>
> ```
> Input: lists = []
> Output: []
> ```
>
> **Example 3:**
>
> ```
> Input: lists = [[]]
> Output: []
> ```
>
> **Constraints:**
>
> - `k == lists.length`
> - `0 <= k <= 10^4`
> - `0 <= lists[i].length <= 500`
> - `-10^4 <= lists[i][j] <= 10^4`
> - `lists[i]` is sorted in **ascending order**.
> - The sum of `lists[i].length` won't exceed `10^4`.

## Merge all lists at same time (recursive version)

```cpp
// 05/09/2020
static constexpr auto cmp = [](const ListNode* a, const ListNode *b){return a->val > b->val;};
using Queue = priority_queue<ListNode *, vector<ListNode *>, decltype(cmp)>;
ListNode* mergeKLists(vector<ListNode*>& lists) {
    Queue queue(cmp);
    for(auto l: lists) if(l) queue.push(l);
    return merge_k_lists(queue);
}

ListNode* merge_k_lists(Queue& queue){
    if(queue.empty()) return nullptr;
    auto root = queue.top();
    queue.pop();
    if(root->next)
        queue.push(root->next);
    root->next = merge_k_lists(queue);
    return root;
}
```
## Merge all lists at same time (iterative version) [Gab's solution]

```cpp
ListNode* mergeKLists(vector<ListNode*>& lists) {
    auto cmp = [](auto& n1, auto& n2){ return n1->val > n2->val; };
    priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> nodes(cmp);
    for (auto& list : lists)
        if (list) 
            nodes.push(list);
    if (nodes.empty())
        return nullptr;
    ListNode* merged = nodes.top(), *last = nullptr;
    while (! nodes.empty()) {
        last = last ? last->next = nodes.top() : nodes.top();
        nodes.pop();
        if (last->next)
            nodes.push(last->next);
    }
    last->next = nullptr;
    return merged;
}
```

## Solution with recursive merge of  2 sorted lists

```cpp
// 01/03/2020
ListNode* mergeKLists(vector<ListNode*>& lists) {
    ListNode* merged = NULL;
    for(auto & l:lists)
        merged = merge_sorted_lists(merged, l);
    return merged;
}

ListNode* merge_sorted_lists(ListNode* l1, ListNode* l2) {
    if (l1 && l2) {
        if (l1->val <= l2->val) {
            l1->next = merge_sorted_lists(l1->next, l2);
            return l1;
        } else {
            l2->next = merge_sorted_lists(l1, l2->next);
            return l2;
        }
    } else {
        return (l1) ? l1 : l2;
    }
}
```
## Solution with iterative merge of 2 sorted lists (ugly)

```cpp
ListNode* mergeKLists(vector<ListNode*>& lists) {
    ListNode* merged = NULL;
    for(auto & l:lists)
        merged = merge_sorted_lists(merged, l);
    return merged;
}

ListNode* merge_sorted_lists(ListNode *l1, ListNode *l2){
    if (l1 == NULL)
        return l2;
    if (l2 == NULL)
        return l1;
    bool left = l1->val < l2->val; 
    ListNode *n1 = left?l1->next:l1;
    ListNode *n2 = left?l2:l2->next;
    ListNode* head = left?l1:l2;
    ListNode* last = head;
    last->next = NULL;
    
    while(n1 != NULL && n2 != NULL){
        if (n1->val < n2->val){
            last->next = n1;
            n1 = n1->next;
            last=last->next;
            last->next = NULL;
        }
        else{
            last->next = n2;
            n2 = n2->next;
            last=last->next;
            last->next = NULL;
        }
    }
    if(n1!=NULL)
        last->next = n1;
    else if(n2!=NULL)
        last->next = n2;
    return head;
}
```