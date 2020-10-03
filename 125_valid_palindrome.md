# 125 - Valid Palindrome

[leetcode link](https://leetcode.com/problems/valid-palindrome/)

> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
>
> **Note:** For the purpose of this problem, we define empty string as valid palindrome.
>
> **Example 1:**
>
> ```
> Input: "A man, a plan, a canal: Panama"
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: "race a car"
> Output: false
> ```
>
> **Constraints:**
>
> - `s` consists only of printable ASCII characters.

## Solutions

```cpp
// 03/08/2020
bool isPalindrome(string s) {
    for (auto begin = s.begin(), end = prev(s.end()); begin < end; ++begin, --end){
        while (begin < end && not isalnum(*begin))++begin;
        while (begin < end && not isalnum(*end))--end;
        if (toupper(*begin) != toupper(*end))
            return false;
    }
    return true;
}
```
### variant 1

```cpp
// 03/08/2020
bool isPalindrome(string s) {
    for (auto begin = s.begin(), end = prev(s.end()); begin < end;){
        if (not isalnum(*begin))++begin;
        else if (not isalnum(*end))--end;
        else if (toupper(*begin) == toupper(*end)){
            ++begin; --end;
        }else return false;
    }
    return true;
}
```
### variant 2

```cpp
// 21/04/2020
bool isPalindrome(string s) {
    auto begin = s.begin();
    auto end = prev(s.end());
    if(begin==end)return true;
    while (begin < end){
        if (not isalnum(*begin)){++begin;}
        else if (not isalnum(*end)){--end;}
        else if (toupper(*begin) == toupper(*end)){
            ++begin; --end;
        }else return false;
    }
    return true;
}
```