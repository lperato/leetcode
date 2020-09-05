# 14 - Longest Common Prefix

[leetcode link](https://leetcode.com/problems/longest-common-prefix/)

> Write a function to find the longest common prefix string amongst an array of strings.
>
> If there is no common prefix, return an empty string `""`.
>
> **Note:**
>
> All given inputs are in lowercase letters `a-z`.

## updated solution

```cpp
// 05/09/2020 
string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";
    for(int n = 0, sz = strs.size(), s0 = strs[0].size(); n != s0; ++n){
        char c = strs[0][n];
        for (int i = 1; i != sz; ++i)
            if (n == strs[i].size() || strs[i][n] != c )
                return strs[0].substr(0,n);
    }
    return strs[0];
}
```
## old and ugly solution

```cpp
// 24/02/2020
string longestCommonPrefix(vector<string>& strs) {
    if (strs.size() == 0)
        return string();
    int n = 0;
    bool loop = true;
    while(loop)
    {
        if (n==strs[0].size())
            break;
        char c = strs[0][n];
        for (int i = 1; i<strs.size(); i++)
        {
            if (n==strs[i].size() || strs[i][n] != c )
            {    
                return strs[0].substr(0,n);
            }
        }
        n++;
    }
  
    return strs[0].substr(0,n);
}
```