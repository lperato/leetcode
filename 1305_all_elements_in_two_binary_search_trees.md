# 1305 - All Elements in Two Binary Search Trees

[leetcode link](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)

> Given two binary search trees `root1` and `root2`.
>
> Return a list containing *all the integers* from *both trees* sorted in **ascending** order.
>
> **Constraints:**
>
> - Each tree has at most `5000` nodes.
> - Each node's value is between `[-10^5, 10^5]`.

## Iterative in-order traversal on both trees

```cpp
// 05/09/2020
vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
    vector<int> elements;
    stack<TreeNode *> nodes1;
    stack<TreeNode *> nodes2;
    stack_left_nodes(nodes1, root1);
    stack_left_nodes(nodes2, root2);
    while(!nodes1.empty() || !nodes2.empty()){
        if (nodes2.empty() || (!nodes1.empty() && nodes1.top()->val < nodes2.top()->val))
            iter_tree(elements, nodes1);
        else 
            iter_tree(elements, nodes2);
    }
    return elements;
}

void iter_tree(vector<int>& elements, stack<TreeNode*>& nodes){
    auto ptr = nodes.top();
    nodes.pop(); 
    elements.push_back(ptr->val);
    stack_left_nodes(nodes, ptr->right);
}

void stack_left_nodes(stack<TreeNode*>& nodes, TreeNode* root){
    while(root){
        nodes.push(root);
        root = root->left;
    }
}
```
## DFS in-order on both trees then merge two sorted arrays

```cpp
// 05/09/2020
vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
    vector<int> elt1;
    get_tree_elements(elt1, root1);
    vector<int> elt2;
    get_tree_elements(elt2, root2);
    vector<int> elements(elt1.size() + elt2.size());
    for(int i=0, i1=0, i2=0, s1=elt1.size(), s2=elt2.size(); i != s1+s2;++i)
        elements[i] = (i2 == s2 ||(i1 != s1 && elt1[i1]<elt2[i2]))?elt1[i1++]:elt2[i2++];
    return elements;
}

void get_tree_elements(vector<int>& elements, TreeNode* root){
    if(root){
        get_tree_elements(elements, root->left);
        elements.push_back(root->val);
        get_tree_elements(elements, root->right);
    }
}
```
## DFS in-order on both trees + know you STL (Gab's solution)

```cpp
vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
    vector<int> elems;
    inorder(root1, elems);
    auto sz = elems.size();
    inorder(root2, elems);
    inplace_merge(elems.begin(), next(elems.begin(), sz), elems.end());
    return elems;
}

void inorder(TreeNode* root, vector<int>& elems) {
    if (root) {
        inorder(root->left, elems);
        elems.emplace_back(root->val);
        inorder(root->right, elems);
    }
} 
```