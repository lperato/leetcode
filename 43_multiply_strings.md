# 43 - Multiply Strings

[leetcode link](https://leetcode.com/problems/multiply-strings/)

> Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.
>
> **Example 1:**
>
> ```
> Input: num1 = "2", num2 = "3"
> Output: "6"
> ```
>
> **Example 2:**
>
> ```
> Input: num1 = "123", num2 = "456"
> Output: "56088"
> ```
>
> **Note:**
>
> 1. The length of both `num1` and `num2` is < 110.
> 2. Both `num1` and `num2` contain only digits `0-9`.
> 3. Both `num1` and `num2` do not contain any leading zero, except the number 0 itself.
> 4. You **must not use any built-in BigInteger library** or **convert the inputs to integer** directly.

## Solution 

**TODO** rework that solution

```cpp
// 03/03/2020
string multiply(string num1, string num2) {
    if (num1 == "0" || num2 == "0")
        return "0";
    vector<string> tmp; 
    for(int x = num2.size()-1; x>=0; x--){
        tmp.push_back(string(num2.size()-1 -x, '0'));
        int carry = 0;
        for(int y = num1.size()-1; y>=0; y--){
            int n = (num2[x]-'0') * (num1[y]-'0') + carry;
            if (n>9){
                carry = n/10;
                n = n%10;
            }else{
                carry = 0;
            }
            tmp.back().push_back('0'+n);
        }
        if(carry>0)
            tmp.back().push_back('0'+carry);
    }
    string res;
    int x = 0;
    int carry = 0;
    while(x<tmp.back().size()){
        int n = carry;
        for(int i = 0; i < tmp.size() ; i++){
            if(x < tmp[i].size()){
                n += (tmp[i][x] - '0');
            }
        }
        if (n>9){
            carry = n/10;
            n = n%10;
        }else{
            carry = 0;
        }
        res.insert(res.begin(), n+'0');
        x++;
    }
    if (carry>0){
        res.insert(res.begin(), carry+'0');
    }
    return res;
}
```