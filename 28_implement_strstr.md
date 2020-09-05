# 28 - Implement strStr()

[leetcode link](https://leetcode.com/problems/implement-strstr/)

> Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).
>
> Return the index of the first occurrence of needle in haystack, or **-1** if needle is not part of haystack.
>
> **Example 1:**
>
> ```
> Input: haystack = "hello", needle = "ll"
> Output: 2
> ```
>
> **Example 2:**
>
> ```
> Input: haystack = "aaaaa", needle = "bba"
> Output: -1
> ```
>
> **Clarification:**
>
> What should we return when `needle` is an empty string? This is a great question to ask during an interview.
>
> For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).

## Solution

```cpp
// 02/25/2020
int strStr(string haystack, string needle){
    if (needle.empty())
        return 0;
    auto start = haystack.begin();
    auto h = start;
    auto n = needle.begin();
    while (h != haystack.end()){
        if (*h == *n){
            h++;
            n++;
            if (n == needle.end())
                return start - haystack.begin();
        }else{
            n = needle.begin();
            h = ++start;
        }
    }
    return -1;
}
```