# 367 - Valid Perfect Square

[leetcode link](https://leetcode.com/problems/valid-perfect-square/)

> Given a **positive** integer *num*, write a function which returns True if *num* is a perfect square else False.
>
> **Follow up:** **Do not** use any built-in library function such as `sqrt`.
>
> **Example 1:**
>
> ```
> Input: num = 16
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: num = 14
> Output: false
> ```

## Solution 1: compute successive squares till *num* 

```cpp
// 09/05/2020
bool isPerfectSquare(int num) {
    if(num == 1) return true;
    for(long i = 2; i <= num/2; i++){
        long tmp = i*i;
        if(tmp == num)
            return true;
        if(tmp>num) return false;
    }
    return false;
}
```
## Solution 2: compute successive squares till *num* using additions only

```cpp
// 09/05/2020
// (x + 1)^2 = x^2 + 2x + 1;
bool isPerfectSquare(int num) {
    if(num == 1) return true;
    long x2 = 1; 
    int x = 1;
    while(x2 < num){
        x2 = x2 + 2 * x + 1;
        if(x2 == num)
            return true;
        ++x;
    }
    return x2 == num;
}
```
Shorter version:

```cpp
// 09/05/2020
bool isPerfectSquare(int num) {
    if(num == 1) return true;
    long x2 = 1; 
    int x = 1;
    while(x2 < num) x2 += 2 * x++ + 1;
    return x2 == num;
}
```
## Solution 3: use binary search

```cpp
// 20/09/2020
bool isPerfectSquare(int num) {
    if(num == 1) return true;
    int l = 1, r = num/2 +1;
    while(l < r){
        int mid = l + (r -l)/2;
        int64_t mid2 = (int64_t)mid * mid;
        if(mid2 < num)
            l = mid+1;
        else if(mid2 > num)
            r = mid;
        else return true;
    }
    return false;
}
```