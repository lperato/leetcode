# 67 - Add Binary

[leetcode link](https://leetcode.com/problems/add-binary/)

> Given two binary strings, return their sum (also a binary string).
>
> The input strings are both **non-empty** and contains only characters `1` or `0`.
>
> **Example 1:**
>
> ```
> Input: a = "11", b = "1"
> Output: "100"
> ```
>
> **Example 2:**
>
> ```
> Input: a = "1010", b = "1011"
> Output: "10101"
> ```
>
>  
>
> **Constraints:**
>
> - Each string consists only of `'0'` or `'1'` characters.
> - `1 <= a.length, b.length <= 10^4`
> - Each string is either `"0"` or doesn't contain any leading zero.

## Solution 1

```cpp
// 19/07/2020
string addBinary(string a, string b){
    string result(max(a.size(),b.size()), 0);
    bool carry = false;
    for(int i = a.size()-1, j = b.size()-1, k=result.size()-1; i>=0 || j>=0; k--){
        bool bit_a = !(i<0 || !(a[i--]-'0'));
        bool bit_b = !(j<0 || !(b[j--]-'0'));
        result[k] = '0'+(bit_a != bit_b != carry);
        carry = (bit_a && bit_b) || (bit_a && carry) || (bit_b && carry);
    }
    return carry?"1"+result:result;
}
```
## Solution 2

```cpp
// 21/05/2020
string addBinary(string a, string b) {
    string& longstr = a.size() > b.size()?a:b;
    string& shortstr = a.size() > b.size()?b:a;
    int lsize = longstr.size();
    int ssize = shortstr.size();
    char carry = 0;
    for(int i = 1; i <= ssize; ++i){ 
        char lc = longstr[lsize-i] - '0';
        char sc = shortstr[ssize-i]- '0';
        longstr[lsize-i] = '0'+(lc ^ sc ^ carry);
        carry = (lc & sc) | ((lc | sc)&carry);
    }
    for(int i = lsize-1-ssize; i >= 0; --i){ 
        char lc = longstr[i] - '0';
        longstr[i] = '0'+(lc ^ carry);
        carry = lc&carry;
    }
    return carry?"1"+longstr:longstr;
}
```
