# 166 - Fraction to Recurring Decimal

[leetcode link](https://leetcode.com/problems/fraction-to-recurring-decimal/)

> Given two integers representing the `numerator` and `denominator` of a fraction, return *the fraction in string format*.
>
> If the fractional part is repeating, enclose the repeating part in parentheses.
>
> If multiple answers are possible, return **any of them**.
>
> **Example 1:**
>
> ```
> Input: numerator = 1, denominator = 2
> Output: "0.5"
> ```
>
> **Example 2:**
>
> ```
> Input: numerator = 2, denominator = 1
> Output: "2"
> ```
>
> **Example 3:**
>
> ```
> Input: numerator = 2, denominator = 3
> Output: "0.(6)"
> ```
>
> **Example 4:**
>
> ```
> Input: numerator = 4, denominator = 333
> Output: "0.(012)"
> ```
>
> **Example 5:**
>
> ```
> Input: numerator = 1, denominator = 5
> Output: "0.2"
> ```
>
> **Constraints:**
>
> - `-231 <= numerator, denominator <= 231 - 1`
> - `denominator != 0`

## Solution

```cpp
// 26/04/20
string fractionToDecimal(int numerator, int denominator) {
    stringstream s;
    long q = (long)numerator / denominator;
    long rest = numerator - q * denominator;
    if (q == 0 
    && ((numerator<0 && denominator>0) ||(numerator>0 && denominator<0))) 
        s << '-';
    s << q;
    if (rest!=0){
        s << '.';
        unordered_map<long, int> restdec;
        rest *= 10;
        int dec = 0;
        while (rest!=0){
            auto it = restdec.find(rest);
            if (it == restdec.end()){
                restdec[rest] = dec++;
                q = rest / denominator;
                s << abs(q);
                rest -= q * denominator;
                rest *= 10;
            }
            else{
                s << ')';
                auto result = s.str();
                result.insert(result.begin()+result.size()-dec+it->second-1, '(');
                return result;
            }
        }
    }
    return s.str();
}
```
