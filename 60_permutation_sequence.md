# 60 - Permutation Sequence

[leetcode link](https://leetcode.com/problems/permutation-sequence/)

> The set `[1,2,3,...,*n*]` contains a total of *n*! unique permutations.
>
> By listing and labeling all of the permutations in order, we get the following sequence for *n* = 3:
>
> 1. `"123"`
> 2. `"132"`
> 3. `"213"`
> 4. `"231"`
> 5. `"312"`
> 6. `"321"`
>
> Given *n* and *k*, return the *k*th permutation sequence.
>
> **Note:**
>
> - Given *n* will be between 1 and 9 inclusive.
> - Given *k* will be between 1 and *n*! inclusive.
>
> **Example 1:**
>
> ```
> Input: n = 3, k = 3
> Output: "213"
> ```
>
> **Example 2:**
>
> ```
> Input: n = 4, k = 9
> Output: "2314"
> ```

## Solution

```cpp
//02/04/2020
string getPermutation(int n, int k) {
    int f = factorial(n);
    string res;
    std::vector<bool> used(n, false);
    int p = 0;
    int K = k-1;
    for(int i = n; i > 0; i--){
        f = f / i;
        int c = K / f;
        int letter = get_nth_letter(used, c);
        used[letter] = true;
        res.push_back(1+letter+'0');
        K -= c*f;
    }
    return res;
}

int factorial(int n){
    return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

int get_nth_letter(const std::vector<bool>& used, int n){
    int i=0;
    int k=0;
    while(i <= n && k != used.size()){
        if(!used[k])
            i++;
        k++;
    }
    return k-1;
}  
```