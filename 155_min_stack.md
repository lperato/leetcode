# 155 - Min Stack

[leetcode link](https://leetcode.com/problems/min-stack/)

> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
>
> - push(x) -- Push element x onto stack.
> - pop() -- Removes the element on top of the stack.
> - top() -- Get the top element.
> - getMin() -- Retrieve the minimum element in the stack.
>
> **Example 1:**
>
> ```
> Input
> ["MinStack","push","push","push","getMin","pop","top","getMin"]
> [[],[-2],[0],[-3],[],[],[],[]]
> 
> Output
> [null,null,null,null,-3,null,0,-2]
> 
> Explanation
> MinStack minStack = new MinStack();
> minStack.push(-2);
> minStack.push(0);
> minStack.push(-3);
> minStack.getMin(); // return -3
> minStack.pop();
> minStack.top();    // return 0
> minStack.getMin(); // return -2
> ```
>
> **Constraints:**
>
> - Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.

## Solution

```cpp
class MinStack {
public:
    /** initialize your data structure here. */
    vector<int> _vec;
    vector<int> _min;
    MinStack(){}
    
    void push(int x) {
        if(_vec.empty() || x < _vec[_min.back()]){
            _min.push_back(_vec.size());
        }
        _vec.push_back(x);
    }
    
    void pop() {
        if (_vec.empty())
            return;
        if(_vec.size() -1 == _min.back())
            _min.pop_back();
        _vec.pop_back();
    }
    
    int top() {
        return _vec.back();
    }
    
    int getMin() {
        return _vec[_min.back()];
    }
};
```