# 150 - Evaluate Reverse Polish Notation

[leetcode link](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

> Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).
>
> Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.
>
> **Note:**
>
> - Division between two integers should truncate toward zero.
> - The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
>
> **Example 1:**
>
> ```
> Input: ["2", "1", "+", "3", "*"]
> Output: 9
> Explanation: ((2 + 1) * 3) = 9
> ```
>
> **Example 2:**
>
> ```
> Input: ["4", "13", "5", "/", "+"]
> Output: 6
> Explanation: (4 + (13 / 5)) = 6
> ```
>
> **Example 3:**
>
> ```
> Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
> Output: 22
> Explanation: 
>   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
> = ((10 * (6 / (12 * -11))) + 17) + 5
> = ((10 * (6 / -132)) + 17) + 5
> = ((10 * 0) + 17) + 5
> = (0 + 17) + 5
> = 17 + 5
> = 22
> ```

## Solution

```cpp
// 18/04/2020
int evalRPN(vector<string>& tokens) {
    return eval_rpn(tokens, tokens.size()-1)[0];
}

array<int,2> eval_rpn(vector<string>& tokens, int i){
    const string& token = tokens[i];
    if(token == "-"){
        auto right = eval_rpn(tokens, i-1);
        auto left = eval_rpn(tokens, right[1]);
        return {left[0] - right[0], left[1]}; 
    }else if(token == "+"){
        auto right = eval_rpn(tokens, i-1);
        auto left = eval_rpn(tokens, right[1]);
        return {left[0] + right[0], left[1]}; 
    }else if(token == "*"){
        auto right = eval_rpn(tokens, i-1);
        auto left = eval_rpn(tokens, right[1]);
        return {left[0] * right[0], left[1]}; 
    }else if(token == "/"){
        auto right = eval_rpn(tokens, i-1);
        auto left = eval_rpn(tokens, right[1]);
        return {left[0] / right[0], left[1]}; 
    }
    else{
        return {atoi(token.c_str()), i-1};
    }
}
```