# 108 - Convert Sorted Array to Binary Search Tree

[leetcode link](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

> Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
>
> For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every* node never differ by more than 1.
>
> **Example:**
>
> ```
> Given the sorted array: [-10,-3,0,5,9],
> 
> One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
> 
>       0
>      / \
>    -3   9
>    /   /
>  -10  5
> ```

## Iterative solution

```cpp
// 27/04/2020
TreeNode* sortedArrayToBST(vector<int>& nums) {
    auto it = nums.begin();
    TreeNode* root = nullptr;
    TreeNode* prev = nullptr;
    TreeNode* left
    while(it != nums.end()){
        TreeNode* node = new TreeNode(*it);
        ++it;
        prev = node;
    }
}
```
## Recursive solution

```cpp
// 27/04/2020
// Runtime: 44 ms, faster than 15.14% of C++ online submissions 
TreeNode* sortedArrayToBST(vector<int>& nums) {
    return to_bst(nums.begin(), nums.end());
}

TreeNode* to_bst(vector<int>::const_iterator begin, vector<int>::const_iterator end){
    if (begin == end) return nullptr;
    auto mid = begin + (end - begin)/2;
    return new TreeNode(*mid, to_bst(begin, mid), to_bst(mid+1, end));
}
```