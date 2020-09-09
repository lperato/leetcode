# 49 - Group Anagrams

[leetcode link](https://leetcode.com/problems/group-anagrams/)

> Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.
>
> An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the  original letters exactly once.
>
>  
>
> **Example 1:**
>
> ```
> Input: strs = ["eat","tea","tan","ate","nat","bat"]
> Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
> ```
>
> **Example 2:**
>
> ```
> Input: strs = [""]
> Output: [[""]]
> ```
>
> **Example 3:**
>
> ```
> Input: strs = ["a"]
> Output: [["a"]]
> ```
>
>  
>
> **Constraints:**
>
> - `1 <= strs.length <= 104`
> - `0 <= strs[i].length <= 100`
> - `strs[i]` consists of lower-case English letters.

## Solution (very slow :-) )

**TODO** Solve this problem again!

```cpp
// 03/10/2020 
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    map<multiset<char>, vector<string>> m;
    for(const auto& str : strs){
        auto ms = multiset<char>(str.begin(), str.end());
        if (auto it = m.find(ms); it == m.end())
            m.insert (it, {ms, vector<string>(str)});  
        else
            it->second.push_back(str);
    }
    vector<vector<string>> res;
    res.reserve(m.size());
    for(auto const& it: m)
        res.push_back(it.second);
    return res;
}
```