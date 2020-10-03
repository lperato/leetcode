# 140 - Word Break II

[leetcode link](https://leetcode.com/problems/word-break-ii/)

> Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, add spaces in *s* to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
>
> **Note:**
>
> - The same word in the dictionary may be reused multiple times in the segmentation.
> - You may assume the dictionary does not contain duplicate words.
>
> **Example 1:**
>
> ```
> Input:
> s = "catsanddog"
> wordDict = ["cat", "cats", "and", "sand", "dog"]
> Output:
> [
>   "cats and dog",
>   "cat sand dog"
> ]
> ```
>
> **Example 2:**
>
> ```
> Input:
> s = "pineapplepenapple"
> wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
> Output:
> [
>   "pine apple pen apple",
>   "pineapple pen apple",
>   "pine applepen apple"
> ]
> Explanation: Note that you are allowed to reuse a dictionary word.
> ```
>
> **Example 3:**
>
> ```
> Input:
> s = "catsandog"
> wordDict = ["cats", "dog", "sand", "and", "cat"]
> Output:
> []
> ```

## Solution 1

```cpp
using Cache = unordered_map<size_t, vector<string>>;
vector<string> wordBreak(string s, vector<string>& wordDict) {
    Cache cache;
    return word_break(s, wordDict, cache, 0, s.size());
}

const vector<string>& word_break(const string& s, const vector<string>& dict, 
                          Cache& cache, size_t i, size_t j){
    if (auto it = cache.find(i); it!= cache.end())
        return it->second;
    cache[i] = {};
    auto& result = cache[i];
    for (const auto& word: dict){
        if(auto size = word.size(); i+size <= j 
        && equal(word.begin(), word.end(), s.begin()+i, s.begin()+i+size)){
            if(i+size == j)
                result.emplace_back(word);
            else{
                const auto& tmp = word_break(s, dict, cache, i+size, j);
                for(const auto& suffix: tmp){
                    result.emplace_back(word);
                    result.back().push_back(' ');
                    result.back().append(suffix);
                }
            }    
        }
    }
    return result;
}
```
## Variant

```cpp
// string_view based version : dont optimise much but more complex
using Cache = unordered_map<size_t, vector<vector<string_view>>>;
vector<string> wordBreak(string s, vector<string>& wordDict) {
    Cache cache;
    auto & tmp = word_break(s, wordDict, cache, 0, s.size());
    vector<string> result(tmp.size());
    for(int i=0, size=tmp.size(); i != size; ++i){
        for(const auto& s: tmp[i]){
            result[i].append(s);
            result[i].push_back(' ');
        }
        result[i].pop_back();
    }
    return result;
}

const vector<vector<string_view>>& word_break(const string& s, const vector<string>& dict, 
                          Cache& cache, size_t i, size_t j){
    if (auto it = cache.find(i); it!= cache.end())
        return it->second;
    cache[i] = {};
    auto& result = cache[i];
    for (const auto& word: dict){
        if(auto size = word.size(); i+size <= j 
        && equal(word.begin(), word.end(), s.begin()+i, s.begin()+i+size)){
            if(i+size == j)
                result.emplace_back(1, word);
            else{
                const auto& tmp = word_break(s, dict, cache, i+size, j);
                for(const auto& suffix: tmp){
                    result.emplace_back();
                    auto &back = result.back();
                    back.reserve(1 + suffix.size());
                    back.emplace_back(word);
                    back.insert(back.end(), suffix.begin(), suffix.end());
                }
            }    
        }
    }
    return result;
}
```