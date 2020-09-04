# 459 - Repeated Substring Pattern

[leetcode link](https://leetcode.com/problems/repeated-substring-pattern/)

> Given a non-empty string check if it can be constructed by taking a  substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters  only and its length will not exceed 10000.

## Naïve solution

```cpp
bool repeatedSubstringPattern(string s) {
    for(int i = 1, sz = s.size(); i != sz; ++i){
        if(s[i] == s[0] && sz%i == 0){
            bool repeat = true;
            for(int j = i; j != sz && repeat; j+=i)
                repeat = !s.compare(0, i, s, j, i);
            if(repeat)
                return true;
        }
    }
    return false;
}
```