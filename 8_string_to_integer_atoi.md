# 8 - String to Integer (atoi)

[leetcode link](https://leetcode.com/problems/string-to-integer-atoi/)

> Implement atoi which converts a string to an integer.

```cpp
int myAtoi(string str) {
    bool positive = true;
    auto it = str.begin();
    while(it != str.end() && *it == ' ')++it;
    if(it == str.end())
        return 0;
    if(*it == '+'){
        ++it;
    }
    else if(*it == '-'){
        positive = false;
        ++it;
    }else if(*it < '0' || *it > '9')
        return 0;
    int res = 0;
    while(it != str.end() && *it >= '0' && *it <= '9'){
        res = max<long>((long)res*10 - (*it -'0'), numeric_limits<int>::min());
        ++it;
    }
    if(positive)
        return res==numeric_limits<int>::min()?numeric_limits<int>::max():-res;
    return res;     
}
```