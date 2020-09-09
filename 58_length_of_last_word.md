# 58 -Length of Last Word

[leetcode link](https://leetcode.com/problems/length-of-last-word/)

> Given a string *s* consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
>
> If the last word does not exist, return 0.
>
> **Note:** A word is defined as a **maximal substring** consisting of non-space characters only.
>
> **Example:**
>
> ```
> Input: "Hello World"
> Output: 5
> ```

## Solution

```cpp
// 07/03/2020
int lengthOfLastWord(string s) {
    auto it = s.rbegin();
    for (; it!=s.rend() && *it == ' '; it++);
    int size = 0;
    for (; it!=s.rend() && *it != ' '; it++)
        size++;
    return size;
}  
```