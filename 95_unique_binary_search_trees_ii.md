# 95 - Unique Binary Search Trees II

[leetcode link](https://leetcode.com/problems/unique-binary-search-trees-ii/)

> Given an integer `n`, generate all structurally unique **BST's** (binary search trees) that store values 1 ... *n*.
>
> **Constraints:**
>
> - `0 <= n <= 8`

## Divide & conquer / recursive solution

```cpp
// 02/09/2020
// recursion 
vector<TreeNode*> generateTrees(int n) {
    if(n ==0) return {};
    return generate_trees(1, n);
}

vector<TreeNode*> generate_trees(int from, int to){
    if(from > to) return {nullptr};
    if(from == to) return {new TreeNode(from)};
    vector<TreeNode *> result;
    for(int i = from; i <= to; ++i){
        auto left = generate_trees(from, i-1);
        auto right = generate_trees(i+1, to);
        for(auto l: left){
            for(auto r: right){
                auto node = new TreeNode(i, l, r);
                result.push_back(node);
            }
        }
    }
    return result;
}
```
## Recursion + memoization

```cpp
// 02/09/2020
// recursion + memoization
// Runtime: 12 ms, faster than 92.70% of C++ online submissions for Unique Binary Search Trees II.
// Memory Usage: 9.2 MB, less than 97.88% of C++ online submissions for Unique Binary Search Trees II.
using R = vector<TreeNode *>;
vector<TreeNode*> generateTrees(int n) {
    if(n ==0) return {};
    vector<vector<R>> memo(n+1, vector<R>(n));
    return generate_trees(memo, 1, n);
}

const R& generate_trees(vector<vector<R>>& memo, int from, int to){
    static const R nullptr_entry = {nullptr};
    if(from > to) return nullptr_entry;
    auto &cache = memo[from-1][to-1];
    if(cache.empty()){
        if(from == to) 
            cache.push_back(new TreeNode(from));
        else {
            for(int i = from; i <= to; ++i){
                const auto& left = generate_trees(memo, from, i-1);
                const auto& right = generate_trees(memo, i+1, to);
                for(auto l: left)
                    for(auto r: right)
                        cache.push_back(new TreeNode(i, l, r));
            }
        }
    }
    return cache;
}
```