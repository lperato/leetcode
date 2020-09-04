# 50 - Pow(x, n)

[leetcode link](https://leetcode.com/problems/powx-n/)

> Implement [pow(*x*, *n*)](http://www.cplusplus.com/reference/valarray/pow/), which calculates *x* raised to the power *n* (i.e. xn).
>
> **Constraints:**
>
> - `-100.0 < x < 100.0`
> - `-2^31 <= n <= 2^31-1`
> - `-10^4 <= xn <= 1^04`

## Iterative solution O(1) time (using bit shifting)

```cpp
// iterative solution O(1) time
double myPow(double x, int n) {
    double res = 1.0;
    bool neg = n<0;
    n = abs(n);
    for(int shift = 0; shift<32; shift++){
        res = (n & (1 << shift))?res*x:res;
        x*=x;
    }
    return neg?1.0/res:res;
}
```
## Recursion - O(n) (Fail TLE & stack overflow)

```cpp
// naive recursion O(n) time => stack-overflow on 0.00001 ^ 2147483647
double myPow(double x, int n) {
    if(n == 0) return 1;
    else if(n>0) return x * myPow(x, n -1);
    else return 1.0 / myPow(x, -n);
}
```
## Tail recursion - O(n) with a bit of tweaking...

```cpp
// tail recursion O(n)
double myPow(double x, int n) {
    if(x == 0) return 0;
    if(abs(x) == 1) return n%2?x:abs(x);
    double result = 1;
    if(n>0) my_pow(x, result, n);
    else my_pow(x, result, -(long)n);
    return n>0?result:(result>100000?0:1/result);
}

void my_pow(double x, double &result, uint n){
    if(result == 0 || n == 0 || abs(result) > 100000) return;
    result *= x;
    my_pow(x, result, n-1);
}
```
## Testcases to consider

```
0.00001
2147483647
1.00000
2147483647
3.76050
-8
2.00000
-2147483648
-1.00000
2147483647
```

