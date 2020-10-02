# 639 - Decode Ways II

[leetcode link](https://leetcode.com/problems/decode-ways-ii/)

> A message containing letters from `A-Z` is being encoded to numbers using the following mapping way:
>
> ```
> 'A' -> 1
> 'B' -> 2
> ...
> 'Z' -> 26
> ```
>
> Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.
>
> Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
>
> Also, since the answer may be very large, you should return the output mod 109 + 7.
>
> **Example 1:**
>
> ```
> Input: "*"
> Output: 9
> Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
> ```
>
> **Example 2:**
>
> ```
> Input: "1*"
> Output: 9 + 9 = 18
> ```
>
> **Note:**
>
> 1. The length of the input string will fit in range [1, 105].
> 2. The input string will only contain the character '*' and digits '0' - '9'.

**TODO** Provide DP solution

## Recursion + memoization

```cpp
// 26/09/2020
// recursion + memo
int numDecodings(string s) {
    vector<int> memo(s.size(), -1);
    return num_decodings(s, memo)%1000000007;
}

int num_decodings(const string& s, vector<int>& memo, int i = 0){
    if(i>=s.size()) return 1;
    if(memo[i] == -1){
        if(i==s.size()-1) 
            memo[i] = s[i]=='*'?9:(s[i]!='0');
        else {
            memo[i] = 0;
            if(s[i] != '0'){
                int n2 = two_chars_comb(s[i], s[i+1]);
                memo[i] = (s[i]=='*'?9:1)*num_decodings(s, memo, i+1)
                        + (n2 == 0?0:n2*num_decodings(s, memo, i+2));
            }
        }
    }
    return memo[i];
}

int two_chars_comb(char c1, char c2){
    if(c1 != '*' && c2 != '*')
        return ((c1-'0') * 10) + c2-'0' <= 26;
    else if(c1 == '*' && c2 == '*')
        return 15;
    else if(c1 == '*')
        return 1 + (c2-'0' < 7);
    else{
        if(c1 == '1') return 9;
        else if(c1 == '2') return 6;
        else return 0;
    }
}
```