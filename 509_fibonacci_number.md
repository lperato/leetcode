# 509 - Fibonacci Number

[leetcode link](https://leetcode.com/problems/fibonacci-number/)

>The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
```

>  Given `N`, calculate `F(N)`.

## Recursion 

```cpp
// recursion - doesnt TLE! :-)
int fib(int N) {
    if(N < 2) return N;
    return fib(N - 1) + fib(N - 2);
}
```


## Recursion + memoization

```cpp
// recursion + memoization
int fib(int N) {
    if(N < 2) return N;
    vector<int> memo(N+1, -1);
    memo[0] = 0; memo[1] = 1;
    return fib(memo, N);
}

int fib(vector<int>& memo, int n){
    if(memo[n] == -1)
        memo[n] = fib(memo, n-1) + fib(memo, n-2);
    return memo[n];
}
```