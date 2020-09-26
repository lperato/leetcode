# 91 - Decode Ways

[leetcode link](https://leetcode.com/problems/decode-ways/)

> A message containing letters from `A-Z` is being encoded to numbers using the following mapping:
>
> ```
> 'A' -> 1
> 'B' -> 2
> ...
> 'Z' -> 26
> ```
>
> Given a **non-empty** string containing only digits, determine the total number of ways to decode it.
>
> **Example 1:**
>
> ```
> Input: "12"
> Output: 2
> Explanation: It could be decoded as "AB" (1 2) or "L" (12).
> ```
>
> **Example 2:**
>
> ```
> Input: "226"
> Output: 3
> Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
> ```

## Recursion  - TLE

```cpp
// 23/09/2020
int numDecodings(string s) {
    return num_decodings(s);
}

int num_decodings(const string& s, int i = 0){
    if(i>=s.size()) return 1;
    if(i==s.size()-1) return s[i]!='0';
    int n = 10*(s[i]-'0')+s[i+1]-'0';
    return (s[i]!='0'?num_decodings(s, i+1):0) + (s[i] !='0' && n<=26?num_decodings(s, i+2):0);
}
```
## Recursion + memoization

```cpp
// 23/09/2020
// recursion + memo
int numDecodings(string s) {
    vector<int> memo(s.size(), -1);
    return num_decodings(s, memo);
}

int num_decodings(const string& s, vector<int>& memo, int i = 0){
    if(i>=s.size()) return 1;
    if(memo[i] == -1){
        if(i==s.size()-1) 
            memo[i] = s[i]!+'0';
        else {
            int n = 10*(s[i]-'0')+s[i+1]-'0';
            memo[i] = (s[i] != '0'? num_decodings(s, memo, i+1): 0) 
                    + (s[i] != '0' && n<=26? num_decodings(s, memo, i+2): 0);
        }
    }
    return memo[i];
}
```
## Old solution [ugly]

```cpp
// 30/03/2020
int numDecodings(string s) {
    if (s.empty())
        return 0;
    vector<int> num(s.size(), 0);
    
    int i = s.size() - 1;
    num[i] = (s[i] == '0'?0:1);
    if (i == 0)
        return num[0];
    i--;
    num[i] = (s[i] == '0'?0:num[i+1]);
    if(s[i] == '1' || (s[i] == '2' && s[i+1] < '7')){
         num[i]++;
    }
    if (i == 0)
        return num[0];
    i--;
    for(; i>=0; i--){
        if(s[i]!='0')
            num[i] = num[i+1];
        if(s[i] == '1' || (s[i] == '2' && s[i+1] < '7')){
            num[i] += num[i+2];
        }
    }
    return num[0];
}
```