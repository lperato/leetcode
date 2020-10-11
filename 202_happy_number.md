# 202 - Happy Number

[leetcode link](https://leetcode.com/problems/happy-number/)

> Write an algorithm to determine if a number `n` is "happy".
>
> A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where  it will stay), or it **loops endlessly in a cycle** which does not include 1. Those numbers for which this process **ends in 1** are happy numbers.
>
> Return True if `n` is a happy number, and False if not.
>
> **Example:** 
>
> ```
> Input: 19
> Output: true
> Explanation: 
> 12 + 92 = 82
> 82 + 22 = 68
> 62 + 82 = 100
> 12 + 02 + 02 = 1
> ```

## solution

```cpp
// 02/04/2020
bool isHappy(int n){
    unordered_set<int> nums;
    return isHappy(n, nums);
}

bool isHappy(int n, unordered_set<int>& nums)  {
    int m = n;
    int num = 0;
    while(m>0){
        int d = m%10;
        num += d * d;
        m = m/10;
    }
    if (num == 1)
        return true;
    if (num == n)
        return false;
    auto it = nums.find(num);
    if (it != nums.end())
        return false;
    nums.insert(n);
    return isHappy(num, nums);
}
```