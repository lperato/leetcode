# 24 - Swap Nodes in Pairs

[leetcode link](https://leetcode.com/problems/swap-nodes-in-pairs/)

## Recursive solution

```cpp
    ListNode* swapPairs(ListNode* head){
        if(!head) return nullptr;
        if(!head->next) return head;
        auto new_head = head->next;
        auto tmp = new_head->next;
        new_head->next = head;
        head->next = swapPairs(tmp);
        return new_head;
    }
```

## Iterative solution (ugly version)

```cpp
ListNode* swapPairs(ListNode* head) {
    auto node = head;
    ListNode *res = NULL;
    ListNode *last = NULL;
    while(node!=NULL){
        auto next = node->next;
        if (next != NULL){
            auto nextnext = next->next;
            if(res==NULL){
                res = next;
                res->next = node;
            }  else{
                last->next = next;
                next->next = node;
        	}
            last = node;
            last->next = NULL;
            node = nextnext;
        }
        else{
            if(res==NULL){
            	return node;
            } else {
                last->next = node;
                return res;
            }
        }
    }
    return res;
}
```