# 449 - Serialize and Deserialize BST

[leetcode link](https://leetcode.com/problems/serialize-and-deserialize-bst/)

> Serialization  is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a  network connection link to be reconstructed later in the same or another computer environment.
>
> Design an algorithm to serialize and deserialize a **binary search tree**. There is no restriction on how your serialization/deserialization  algorithm should work. You need to ensure that a binary search tree can  be serialized to a string, and this string can be deserialized to the  original tree structure.
>
> **The encoded string should be as compact as possible.**
>
> **Example 1:**
>
> ```
> Input: root = [2,1,3]
> Output: [2,1,3]
> ```
>
> **Example 2:**
>
> ```
> Input: root = []
> Output: []
> ```
>
> **Constraints:**
>
> - The number of nodes in the tree is in the range `[0, 104]`.
> - `0 <= Node.val <= 104`
> - The input tree is **guaranteed** to be a binary search tree.

## Solution

**TODO** Find a simpler way to deserialize BST from preorder(ed) array of values

```cpp
// 09/10/2020

// Encodes a tree to a single string.
string serialize(TreeNode* root) {
    string treestring;
    serialize_preorder_dfs(root, treestring);
    return treestring;
}

void serialize_preorder_dfs(TreeNode *root, string& s){
    if(root){
        s.append(to_string(root->val));
        s.push_back(' ');
        serialize_preorder_dfs(root->left, s);
        serialize_preorder_dfs(root->right, s);
    }
}

// Decodes your encoded data to tree.
TreeNode* deserialize(string data) {
    istringstream iss(data);
    int val;
    vector<int> values;
    while(iss >> val)
        values.push_back(val);
    auto it = values.cbegin();
    return deserialize_preorder(it, values.end());
}

using IT = vector<int>::const_iterator;
TreeNode * deserialize_preorder(IT& it, IT end, TreeNode* right_parent=nullptr){
    if(it == end) 
        return nullptr;
    auto node = new TreeNode(*it++);
    if(it != end && *it < node->val)
        node->left = deserialize_preorder(it, end, node);
    if(it != end && (right_parent == nullptr || right_parent->val > *it))
        node->right = deserialize_preorder(it, end, right_parent);
    return node;
}
```