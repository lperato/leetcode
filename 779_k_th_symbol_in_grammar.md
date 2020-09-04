# 779 - K-th Symbol in Grammar

[leetcode link](https://leetcode.com/problems/k-th-symbol-in-grammar/)

>On the first row, we write a `0`. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.
>
>Given row `N` and index `K`, return the `K`-th indexed symbol in row `N`. (The values of `K` are 1-indexed.) (1 indexed).

## Brute force recursive solution (TLE)

```cpp
// 02/09/2020
// naive brute force recursive solution => TLE
int kthGrammar(int N, int K) {
    return kth_grammar(N)[K-1];
}

vector<bool> kth_grammar(int n){
    if(n==1) return {0};
    auto row = kth_grammar(n-1);
    vector<bool> result(row.size()*2);
    for(int i = 0, s = row.size(); i != s; ++i){
        result[i*2] = row[i];
        result[i*2+1] = !row[i];
    }
    return result;
}
```
## Recursive solution = f(k)

```cpp
// 02/09/2020
// recursive solution = f(k) k = K-1
// f(k) = !f(k/2) if k%2 == 0
//        !f(k-1) if k%2 == 1
// f(0) = 0
int kthGrammar(int N, int K) {
    if(K == 1) return 0;
    if((K-1)%2 == 0) return kthGrammar(0, (K-1)/2+1);
    return !kthGrammar(0, K-1);
}
```
