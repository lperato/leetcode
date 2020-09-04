# 5 - Longest Palindromic Substring

[leetcode link](https://leetcode.com/problems/longest-palindromic-substring/)

> Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

**TODO: ** rework that ugly solution :-)

```cpp
string longestPalindrome(string s) {
    auto p_begin = s.end();
    auto p_end = s.end();
    size_t max_size = 0;
    for (auto it = s.begin(); it != s.end(); ++it){
        auto begin = it;
        auto end = it+1;
        while(true){
            auto size = end - begin;
            if (size > max_size){
                max_size = size;
                p_begin = begin;
                p_end = end;
            }
            if(begin != s.begin() && end != s.end() && *(begin-1) == *end ){
                begin--;
                end++;
            }
            else
                break;
        }
        if (*it == *(it+1)){
            begin = it;
            end = it+2;
            while(true){
                auto size = end - begin;
                if (size > max_size){
                    max_size = size;
                    p_begin = begin;
                    p_end = end;
                }
                if(begin != s.begin() && end != s.end() && *(begin-1) == *end ){
                    begin--;
                    end++;
                }
                else
                    break;
            }
        }
    }
    return string(p_begin, p_end);
}
```
