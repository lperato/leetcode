# 3 - Longest Substring Without Repeating Characters

[leetcode link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

> Given a string, find the length of the longest substring without repeating characters.

```cpp
int lengthOfLongestSubstring(string s) {
    int max_len = 0;
    int len = 0;
    auto it = s.begin();
    bitset<256> letters;
    len = 0;
    while(it!= s.end()){
        if (letters[*it]){
            len--;
            it++;
        }else{
            letters.set(*it);
            len++;
            if (len>max_len)
                max_len = len;
            it++;
        }
    }
    return max_len;
}
```
    