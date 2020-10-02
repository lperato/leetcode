# 139 - Word Break

[leetcode link](https://leetcode.com/problems/word-break/)

> Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, determine if *s* can be segmented into a space-separated sequence of one or more dictionary words.
>
> **Note:**
>
> - The same word in the dictionary may be reused multiple times in the segmentation.
> - You may assume the dictionary does not contain duplicate words.
>
> **Example 1:**
>
> ```
> Input: s = "leetcode", wordDict = ["leet", "code"]
> Output: true
> Explanation: Return true because "leetcode" can be segmented as "leet code".
> ```
>
> **Example 2:**
>
> ```
> Input: s = "applepenapple", wordDict = ["apple", "pen"]
> Output: true
> Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
>              Note that you are allowed to reuse a dictionary word.
> ```
>
> **Example 3:**
>
> ```
> Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
> Output: false
> ```

## Recursion - TLE

```cpp
// 30/07/2020
bool wordBreak(string s, vector<string>& wordDict) {
    return word_break(s, wordDict, 0, s.size());
}

bool word_break(const string& s, const vector<string>& dict, size_t i, size_t j){
    if (i==j) return true;
    for (const auto& word: dict){
        auto size = word.size();
        if(i+size<=j 
        && equal(word.begin(), word.end(), s.begin()+i, s.begin()+i+size)
        && word_break(s, dict, i+size, j))
            return true;
    }
    return false;
}
```
## Recursion + memoization

```cpp
// 30/07/2020
// indices + unordered_map
using Memo = unordered_map<size_t, bool>;
bool wordBreak(string s, vector<string>& wordDict) {
    Memo memo;
    return word_break(s, wordDict, memo, 0, s.size());
}

bool word_break(const string& s, const vector<string>& dict, Memo& memo, 
                size_t i, size_t j){
    if (i==j) 
        return true;
    if (auto it = memo.find(i); it!= memo.end())
        return it->second;
    else{
        auto &mem = memo[i];
        for (const auto& word: dict){
            auto size = word.size();
            if(i+size<=j 
            && equal(word.begin(), word.end(), s.begin()+i, s.begin()+i+size)
            && word_break(s, dict, memo, i+size, j)){
                mem = true;
                break;
            }
        }
        return mem;
    } 
}
```
### Older variant using iterators

```cpp
// 19/04/2020
//iterators + map<string, bool>
bool wordBreak(string s, vector<string>& wordDict) {
    map<string::const_iterator, bool> cache;
    return word_break(s.begin(), s.end(), wordDict, cache);
}

bool word_break(string::const_iterator begin,
                string::const_iterator end,
                vector<string>& dict, 
                map<string::const_iterator, bool>& cache){
    if (begin==end) 
        return true;
    auto it = cache.find(begin);
    if (it!= cache.end()){
        return it->second;
    }
    for (const auto& word: dict){
        auto size = word.size();
        if(begin+size<=end 
        && equal(word.begin(), word.end(), begin, begin+size)){
            if (word_break(begin+size, end, dict, cache)){
                cache[begin] = true;
                return true;
            }
        }
    }
    cache[begin] = false;
    return false;
}
```
**TODO:** Write the DP solution!