# 22 - Generate Parentheses

[leetcode link](https://leetcode.com/problems/generate-parentheses/)

> Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
>
> For example, given *n* = 3, a solution set is:
>
> ```
> [
>   "((()))",
>   "(()())",
>   "(())()",
>   "()(())",
>   "()()()"
> ]
> ```

## Solution

```cpp
// 27/02/2020
vector<string> generateParenthesis(int n) {
    return gen(n);
}

vector<string> gen(int n, const string& base="", int depth=0){
    if (base.size() == 2*n - 1){
        return vector<string>{base+")"};
    }
    vector<string> res;
    if(depth>0){
        auto tmp = gen(n, base+")", depth-1);
        res.insert(res.end(), tmp.begin(), tmp.end());
    }
    if(depth < n && depth < 2*n - base.size()){
        auto tmp = gen(n, base+"(", depth+1); 
        res.insert(res.end(), tmp.begin(), tmp.end());
    }
    return res;
}
```