# 204 - Count Primes

[leetcode link](https://leetcode.com/problems/count-primes/)

> Count the number of prime numbers less than a non-negative number, `n`.
>
> **Example 1:**
>
> ```
> Input: n = 10
> Output: 4
> Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
> ```
>
> **Example 2:**
>
> ```
> Input: n = 0
> Output: 0
> ```
>
> **Example 3:**
>
> ```
> Input: n = 1
> Output: 0
> ```
>
> **Constraints:**
>
> - `0 <= n <= 5 * 106`

## Solution 1 - naïve  approach

```cpp
// 23/05/2020
int countPrimes(int n) {
    int count = 0;
    for(int i = 2; i < n; ++i){
        if(is_prime(i)) 
            ++count;
    }
    return count;
}

bool is_prime(int n){
    if (n <= 1) return false;
    for(int i = 2; i * i <= n; ++i){
        if(i*(int)(n/i) == n)
            return false;
    }
    return true;
}
```
## Solution 2 - DP like approach

```cpp
// 23/05/2020
int countPrimes(int n) {
    if(n<3) return 0;
    vector<bool> is_prime(n, true);
    for(int i = 2; i*i<n; ++i){
        if (!is_prime[i]) 
            continue;            
        for (int j = i*i; j < n; j+=i)
            is_prime[j] = false;
    }
    int count = 0;
    for(int i = 2; i<n; ++i)
    	count += is_prime[i];
    return count;
}
```