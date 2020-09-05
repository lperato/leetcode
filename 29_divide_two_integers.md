# 29 - Divide Two Integers

[leetcode link](https://leetcode.com/problems/divide-two-integers/)

> Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division and mod operator.
>
> Return the quotient after dividing `dividend` by `divisor`.
>
> The integer division should truncate toward zero, which means losing its fractional part. For example, `truncate(8.345) = 8` and `truncate(-2.7335) = -2`.
>
> **Note:**
>
> - Both dividend and divisor will be 32-bit signed integers.
> - The divisor will never be 0.
> - Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function **returns 231 − 1 when the division result overflows**.

## Solution

```cpp
// 27/02/2020
int divide(int dividend, int divisor) {
    if(dividend == -2147483648 && divisor == -1)
        return 2147483647;
    bool positive = not((dividend >=0) xor (divisor > 0));
    unsigned int n = div(
        dividend < 0?-(long)dividend:dividend,
        divisor < 0?-(long)divisor:divisor); 
    return positive?n:-n;
}

unsigned int div(unsigned int dividend, unsigned int divisor) {
    unsigned int rest = dividend;
    unsigned int n = 0;
    while(divisor <= rest){
        if(divisor == rest)
            return n+1;
        unsigned int k = 1;
        unsigned int d = divisor;
        while( (d << 1) < rest){
            d = d << 1;
            k = k << 1;
        }
        n += k;
        rest-= d;
    }
    return n;
}
```