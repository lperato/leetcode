# 89 - Gray Code

[leetcode link](https://leetcode.com/problems/gray-code/)

> The gray code is a binary numeral system where two successive values differ in only one bit.
>
> Given a non-negative integer *n* representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
>
> **Example 1:**
>
> ```
> Input: 2
> Output: [0,1,3,2]
> Explanation:
> 00 - 0
> 01 - 1
> 11 - 3
> 10 - 2
> 
> For a given n, a gray code sequence may not be uniquely defined.
> For example, [0,2,3,1] is also a valid gray code sequence.
> 
> 00 - 0
> 10 - 2
> 11 - 3
> 01 - 1
> ```
>
> **Example 2:**
>
> ```
> Input: 0
> Output: [0]
> Explanation: We define the gray code sequence to begin with 0.
>              A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
>              Therefore, for n = 0 the gray code sequence is [0].
> ```

## Solution 1 : recursion with copies

```cpp
// 04/04/2020
vector<int> grayCode(int n) {
    if(n==0){
        return vector<int>{0};
    }
    auto codes = grayCode(n-1);
    int size = codes.size();
    codes.resize(2*size);
    for(int i = 0; i < size; i++){
        codes[2*size-i-1] = codes[i] | 1 << (n-1);
    }
    return codes;
}
```
## Solution 2: tail recursion without copies

```cpp
// 23/09/2020
vector<int> grayCode(int n) {
    vector<int> codes(1<<n, 0);
    gray_code(codes, n);
    return codes;
}

void gray_code(vector<int>& codes, int n, int k=0){
    if(k>n) return;
    if(k>0){
        for(int i = 0, N = 1<<(k-1); i != N; ++i)
            codes[2*N-i-1] = codes[i] | N;
    }
    gray_code(codes, n, k+1);
}
```