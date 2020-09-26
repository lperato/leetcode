# 69 - Sqrt(x)

[leetcode link](https://leetcode.com/problems/sqrtx/)

> Implement `int sqrt(int x)`.
>
> Compute and return the square root of *x*, where *x* is guaranteed to be a non-negative integer.
>
> Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
>
> **Example 1:**
>
> ```
> Input: 4
> Output: 2
> ```
>
> **Example 2:**
>
> ```
> Input: 8
> Output: 2
> Explanation: The square root of 8 is 2.82842..., and since 
>              the decimal part is truncated, 2 is returned.
> ```

## Solution 1 : naïve approach

```cpp
// 24/05/2020
int mySqrt(int x) {
    long i = 0;
    for(; i * i <= x; ++i);
    return i-1;
}
```
## Solution 2 : binary search

```cpp
// 18/09/2020
int mySqrt(int x) {
    int l = 0, r = x/2+1;
    while(l<r){
        int mid = l + (r-l)/2;
        if(int64_t mid2 = (int64_t)mid * mid; mid2 < x)
            l = mid+1;
        else if(mid2 > x)
            r = mid;
        else
            return mid;
    }
    return (int64_t)l*l>x?l-1:l;
}
```


```cpp
// 24/05/2020
int mySqrt(int x) {
    int i = 0;
    int j = x/2+1;
    while(i<j){
        long mid = i + (j-i)/2;
        if(mid*mid > x)
            j = mid-1;
        else
            i = mid+1;
    }
    return (long)i*i>x?i-1:i;
}
```