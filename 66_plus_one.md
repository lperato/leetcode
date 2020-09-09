# 66 - Plus One

[leetcode link](https://leetcode.com/problems/plus-one/)

> Given a **non-empty** array of digits representing a non-negative integer, increment one to the integer.
>
> The digits are stored such that the most significant digit is at the  head of the list, and each element in the array contains a single digit.
>
> You may assume the integer does not contain any leading zero, except the number 0 itself.
>
>  
>
> **Example 1:**
>
> ```
> Input: digits = [1,2,3]
> Output: [1,2,4]
> Explanation: The array represents the integer 123.
> ```
>
> **Example 2:**
>
> ```
> Input: digits = [4,3,2,1]
> Output: [4,3,2,2]
> Explanation: The array represents the integer 4321.
> ```
>
> **Example 3:**
>
> ```
> Input: digits = [0]
> Output: [1]
> ```
>
>  
>
> **Constraints:**
>
> - `1 <= digits.length <= 100`
> - `0 <= digits[i] <= 9`

## Solutions

```cpp
// 06/07/2020
vector<int> plusOne(vector<int>& digits) {
    auto size = digits.size();
    vector<int> result(size);
    int carry = 1;
    for(int i = size-1; i >= 0; --i){
        int d = digits[i] + carry;
        result[i] = d>9?0:d;
        carry = d>9?d-9:0;
    }
    if(carry) result.insert(result.begin(), carry);
    return result;
}
```


```cpp
// 27/02/2020
vector<int> plusOne(vector<int>& digits) {
    auto p = digits.end() -1;
    while(p>=digits.begin()){
        if(*p<9){
            *p += 1;
            break;
        }else
            *p = 0;
        p--;
    }
    if(p == digits.begin()-1)
        digits.insert(digits.begin(), 1);
    return digits;
}
```