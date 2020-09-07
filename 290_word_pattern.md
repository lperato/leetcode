# 290 - Word Pattern

[leetcode link](https://leetcode.com/problems/word-pattern/)

> Given a `pattern` and a string `str`, find if `str` follows the same pattern.
>
> Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `str`.
>
> **Example 1:**
>
> ```
> Input: pattern = "abba", str = "dog cat cat dog"
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input:pattern = "abba", str = "dog cat cat fish"
> Output: false
> ```
>
> **Example 3:**
>
> ```
> Input: pattern = "aaaa", str = "dog cat cat dog"
> Output: false
> ```
>
> **Example 4:**
>
> ```
> Input: pattern = "abba", str = "dog dog dog dog"
> Output: false
> ```
>
> **Notes:**
>  You may assume `pattern` contains only lowercase letters, and `str` contains lowercase letters that may be separated by a single space.

## Solution 1

```cpp
// 07/09/2020
bool wordPattern(string pattern, string str) {
    if(pattern.empty()) return false;
    vector<string_view> strv;
    for(int pos = 0, size = str.size(); pos < size;){
        auto p = str.find(' ', pos);
        p = (p==string::npos?size:p);
        strv.emplace_back(&*(str.begin()+pos), p - pos);
        pos = p +1;
    }
    if(pattern.size() != strv.size()) return false;
    array<string_view, 'z' +1> char2word{};
    unordered_map<string_view, char> word2char;
    for(int i = 0, size = strv.size(); i != size; ++i){
        auto &w = char2word[pattern[i]-'a'];
        auto &c = word2char[strv[i]];
        if((!w.empty() && w != strv[i]) || (c && c != pattern[i]))
            return false;
        w = strv[i];
        c = pattern[i];
    }
    return true;
}
```
## Solution 2

```cpp
// 07/07/2020
bool wordPattern(string pattern, string str) {
    array<string_view, 'z'+1> c_to_str;
    unordered_map<string_view, char> str_to_c;
    auto size = str.size();
    size_t start = 0; while(str[start] == ' ') start++;
    for(auto c: pattern){
        if(start >= size) return false;
        size_t pos = str.find(' ', start);
        pos = (pos==string::npos)?size:pos;
        string_view s(str.data()+start, pos - start);
        if(c_to_str[c].empty())
            c_to_str[c] = s;
        else if(c_to_str[c] != s) 
            return false;
        if(auto it = str_to_c.find(s); it == str_to_c.end())
            str_to_c.insert({s, c});
        else if(it->second != c) 
            return false;
        start = pos + 1;
    }
    return start == size+1;
}
```

## Gab's solution

```cpp
bool wordPattern(string& pattern, string& str) {
    unordered_map<char, string> to_word;
    unordered_map<string, char> to_char;
    istringstream iss(str);
    istream_iterator<string> word(iss);
    for (auto c : pattern) {
        if (word == istream_iterator<string>()) 
            return false;
        if (auto p = to_word.emplace(c, *word); p.first->second != *word)
            return false;
        if (auto p = to_char.emplace(*word++, c); p.first->second != c)
            return false;
    }
    return word == istream_iterator<string>();
}
```

