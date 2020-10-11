# 171 - Excel Sheet Column Number

[leetcode link](https://leetcode.com/problems/excel-sheet-column-number/)

> Given a column title as appear in an Excel sheet, return its corresponding column number.
>
> For example:
>
> ```
>     A -> 1
>     B -> 2
>     C -> 3
>     ...
>     Z -> 26
>     AA -> 27
>     AB -> 28 
>     ...
> ```
>
> **Example 1:**
>
> ```
> Input: "A"
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: "AB"
> Output: 28
> ```
>
> **Example 3:**
>
> ```
> Input: "ZY"
> Output: 701
> ```
>
> **Constraints:**
>
> - `1 <= s.length <= 7`
> - `s` consists only of uppercase English letters.
> - `s` is between "A" and "FXSHRXW".

## Solution

```cpp
// 10/08/2020
int titleToNumber(string s){
    int num = 0;
    for(auto c : s)
        num = 26 * num - 'A' + c + 1;
    return num;
}
```
### ### Older solution

```cpp
// 16/03/2020
int titleToNumber(string s) {
    unsigned int carry = 1;
    unsigned int n = 0;
    for(auto it = s.rbegin(); it != s.rend(); ++it){
        n += (*it-'A'+1) * carry;
        carry *= 26;
    }
    return n;
}
```