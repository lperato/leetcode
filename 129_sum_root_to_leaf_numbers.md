# 129 - Sum Root to Leaf Numbers

[leetcode link](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

> Given a binary tree containing digits from `0-9` only, each root-to-leaf path could represent a number.
>
> An example is the root-to-leaf path `1->2->3` which represents the number `123`.
>
> Find the total sum of all root-to-leaf numbers.
>
> **Note:** A leaf is a node with no children.
>
> **Example:**
>
> ```
> Input: [1,2,3]
>     1
>    / \
>   2   3
> Output: 25
> Explanation:
> The root-to-leaf path 1->2 represents the number 12.
> The root-to-leaf path 1->3 represents the number 13.
> Therefore, sum = 12 + 13 = 25.
> ```
>
> **Example 2:**
>
> ```
> Input: [4,9,0,5,1]
>     4
>    / \
>   9   0
>  / \
> 5   1
> Output: 1026
> Explanation:
> The root-to-leaf path 4->9->5 represents the number 495.
> The root-to-leaf path 4->9->1 represents the number 491.
> The root-to-leaf path 4->0 represents the number 40.
> Therefore, sum = 495 + 491 + 40 = 1026.
> ```

## Recursive solution

```cpp
// 26/06/2020
int sumNumbers(TreeNode* root, int current=0) {
    if(!root) return 0;
    current = current * 10 + root->val;
    int s = 0;
    if(root->left) s += sumNumbers(root->left, current);
    if(root->right) s += sumNumbers(root->right, current);
    return s==0?current:s;
} 
```
## Ugly recursive solution

```cpp
// 21/04/2020
int sumNumbers(TreeNode* root) {
    vector<int> s;
    return sum_rln(root, s);
}

int sum_rln(TreeNode* node, vector<int>& s){
    if(node == nullptr) return 0;
    if(node->left == nullptr && node->right == nullptr){
        int sum = node->val;
        int n = 1;
        for(int i = s.size()-1; i>=0; i--){
            n *=10;
            sum += s[i]*n;
        }
        return sum;
    }
    int sum = 0;
    if(not s.empty() || node->val !=0)
        s.push_back(node->val);
    sum += sum_rln(node->left, s);
    sum += sum_rln(node->right, s);
    if(not s.empty() || node->val !=0)
        s.pop_back();
    return sum;
}
```