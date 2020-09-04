# 9 - Palindrome Number

[leetcode link](https://leetcode.com/problems/palindrome-number/)

> Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

> Coud you solve it without converting the integer to a string?

# Convert to string, then check if palindromic

**TODO** Rework that solution!

```cpp
bool isPalindrome(int x) {
    if (x < 0)
        return false;
    char num[10];
    int i = 0;
    int n = x;
    while(n > 0){
        num[i] = n%10;
        n = n/10;
        i++;
    }
    n = 0;
    i--;
    while(n < i){
        if (num[n] != num[i])
            return false;
        n++;
        i--;
    }
    return true;
}
```

# Without converting to string

**TODO !**