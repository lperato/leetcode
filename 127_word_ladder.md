# 127 - Word Ladder

[leetcode link](https://leetcode.com/problems/word-ladder/)

> Given two words (*beginWord* and *endWord*), and a dictionary's word list, find the length of shortest transformation sequence from *beginWord* to *endWord*, such that:
>
> 1. Only one letter can be changed at a time.
> 2. Each transformed word must exist in the word list.
>
> **Note:**
>
> - Return 0 if there is no such transformation sequence.
> - All words have the same length.
> - All words contain only lowercase alphabetic characters.
> - You may assume no duplicates in the word list.
> - You may assume *beginWord* and *endWord* are non-empty and are not the same.
>
> **Example 1:**
>
> ```
> Input:
> beginWord = "hit",
> endWord = "cog",
> wordList = ["hot","dot","dog","lot","log","cog"]
> 
> Output: 5
> 
> Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
> return its length 5.
> ```
>
> **Example 2:**
>
> ```
> Input:
> beginWord = "hit"
> endWord = "cog"
> wordList = ["hot","dot","dog","lot","log"]
> 
> Output: 0
> 
> Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
> ```

## Solution

```cpp
int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    if (beginWord == endWord || wordList.empty())
        return 0;
    vector<string> words(1, beginWord);
    return ladder_length(words, endWord, wordList);
}

int ladder_length(const vector<string>&words, 
                  const string& endWord, 
                  vector<string>& wordList, 
                  int distance=0) {
    if (words.empty())        
        return 0;
    vector<string> tmp;
    for (const auto &w : words){
        if(w == endWord){
            return 1+distance;
        }
        for(int i = 0; i < wordList.size(); ++i){
            if (one_letter_diff(w, wordList[i])){
                tmp.push_back(wordList[i]);
                wordList.erase(wordList.begin()+i);
                i--;
            }
        }
    }
    return ladder_length(tmp, endWord, wordList, distance+1);
}

bool one_letter_diff(const string& s1, const string& s2){
    int n = 0;
    for(int i = 0; i < s1.size() && i < s2.size(); i++){
        if (s1[i] != s2[i]){
            n++;
            if(n==2)
                return false;
        }
    }
    n += abs<int>(s1.size() - s2.size());
    return n==1;
}
```