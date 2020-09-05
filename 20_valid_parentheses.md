# 20 - Valid Parentheses

[leetcode link](https://leetcode.com/problems/valid-parentheses/)

> Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
>
> An input string is valid if:
>
> 1. Open brackets must be closed by the same type of brackets.
> 2. Open brackets must be closed in the correct order.
>
> **Constraints:**
>
> - `1 <= s.length <= 104`
> - `s` consists of parentheses only `'()[]{}'`.

## Solution

```cpp
static constexpr char* open = "({[";
bool isValid(string s) {
    stack<char> o;
    for (char c: s){// find if the char is an opening char
        bool found = false;
        for(int i = 0; i < 3; i++){
            if (c == open[i]){
                found = true;
                break;
            }
        }
        if (found){o.push(c);}// if found, add it to the stack
        else{// if not found, pop the element from the stack
             // and check if it is the opposite parentethis
            if (o.empty()){return false;}
            auto x = o.top();
            o.pop();
            if (not is_pair(x, c)){return false;}
        }
    }
    return o.empty();
}

bool is_pair(char c1, char c2){
    return c1 == '(' && c2 == ')'
        || c1 == '{' && c2 == '}'
        || c1 == '[' && c2 == ']';
}
```