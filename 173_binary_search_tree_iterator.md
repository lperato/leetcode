# 173 - Binary Search Tree Iterator

[leetcode link](https://leetcode.com/problems/binary-search-tree-iterator/)

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling `next()` will return the next smallest number in the BST.

**Example:**

**![img](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)**

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
```

**Note:**

- `next()` and `hasNext()` should run in average O(1) time and uses O(*h*) memory, where *h* is the height of the tree.
- You may assume that `next()` call will always be valid, that is, there will be at least a next smallest number in the BST when `next()` is called.

## Solution

```cpp
// 09/04/2020
class BSTIterator {
    TreeNode * current;
    stack<TreeNode*> nodes;
    enum Direction{go_left, go_right};
    Direction direction = go_left;
public:
    BSTIterator(TreeNode* root):current(root) {}

    TreeNode* stack_pop(){
        if(nodes.empty())
            return nullptr;
        TreeNode *tmp = nodes.top();
        nodes.pop();
        return tmp;
    }

    /** @return the next smallest number */
    int next() {
        while(hasNext()){
            if(direction==go_left){
                while(current->left){
                    nodes.push(current);
                    current = current->left;
                }
                direction = go_right;
                return current->val;
            }else{
                if(current->right){
                    direction = go_left;
                    current = current->right;
                } else {
                    direction = go_right;
                    current = stack_pop();
                    if(current)
                        return current->val;
                } 
            }
        }
        return -1;
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return (current && direction == go_left)
            || (current && direction == go_right && (current->right || !nodes.empty()));
    }
};
```
