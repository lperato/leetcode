# 179 - Largest Number

[leetcode link](https://leetcode.com/problems/largest-number/)

> Given a list of non negative integers, arrange them such that they form the largest number.
>
> **Example 1:**
>
> ```
> Input: [10,2]
> Output: "210"
> ```
>
> **Example 2:**
>
> ```
> Input: [3,30,34,5,9]
> Output: "9534330"
> ```
>
> **Note:** The result may be very large, so you need to return a string instead of an integer.

## Solution: transform to_string -> sort -> accumulate

```cpp
// 25/09/2020
string largestNumber(vector<int>& nums) {
    vector<string> v;
    transform(nums.begin(), nums.end(), back_inserter(v), [](int a){return to_string(a);});
    sort(v.begin(), v.end(), [](const string& a, const string& b){return a+b > b+a;});
    return accumulate(v.begin(), v.end(), string("0"), 
                      [](string& a, const string& b){return a=="0"?b:a+b;});
}
```