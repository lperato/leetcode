# 168 - Excel Sheet Column Title

[leetcode link](https://leetcode.com/problems/excel-sheet-column-title/)

> Given a positive integer, return its corresponding column title as appear in an Excel sheet.
>
> For example:
>
> ```
>     1 -> A
>     2 -> B
>     3 -> C
>     ...
>     26 -> Z
>     27 -> AA
>     28 -> AB 
>     ...
> ```
>
> **Example 1:**
>
> ```
> Input: 1
> Output: "A"
> ```
>
> **Example 2:**
>
> ```
> Input: 28
> Output: "AB"
> ```
>
> **Example 3:**
>
> ```
> Input: 701
> Output: "ZY"
> ```

## Solution1

```cpp
// 05/07/2020
string convertToTitle(int n) {
    string result;
    for(n--; n>=0; n= (n/26)-1)
        result.push_back('A'+n%26);
    reverse(result.begin(), result.end());
    return result;
}
```