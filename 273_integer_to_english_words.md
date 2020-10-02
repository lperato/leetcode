# 273 - Integer to English Words

[leetcode link](https://leetcode.com/problems/integer-to-english-words/)

> Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
>
> **Example 1:**
>
> ```
> Input: 123
> Output: "One Hundred Twenty Three"
> ```
>
> **Example 2:**
>
> ```
> Input: 12345
> Output: "Twelve Thousand Three Hundred Forty Five"
> ```
>
> **Example 3:**
>
> ```
> Input: 1234567
> Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
> ```
>
> **Example 4:**
>
> ```
> Input: 1234567891
> Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
> ```

## Solution using recursion

```cpp
// 29/09/2020
string numberToWords(int n) {
    array<string, 16> nums  = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                              "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen"};
    array<string, 5> var = {"Twen", "Thir", "For", "Fif", "Eigh"};
    auto variant = [&nums, &var](int n) ->const string& {if(n < 6) return var[n-2]; return n==8?var[4]:nums[n];};
    const int H = 100, T = 1000, M = 1000 * T, B = 1000 * M;
    if(n < 16)
        return nums[n];
    else if(n < 20)
        return string(variant(n-10))+"teen";
    else if(n < H)
        return string(variant(n/10))+"ty" + (n%10?" " + nums[n%10]:"");
    else if(n < T)
        return nums[n/H] + " Hundred" + (n%H?" "+numberToWords(n%H):"");
    else if(n < M)
        return numberToWords(n/T) + " Thousand" + (n%T?" "+numberToWords(n%T):"");
    else if(n < B)
        return numberToWords(n/M) + " Million" + (n%M?" "+numberToWords(n%M):"");
    return numberToWords(n/B) + " Billion" + (n%B?" "+numberToWords(n%B):"");
}
```
## Nice solutions to look at

[leetcode - C++ 4 lines](https://leetcode.com/problems/integer-to-english-words/discuss/188334/C%2B%2B-4-lines)