# 17 - Letter Combinations of a Phone Number

[leetcode link]()

>Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.
>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
>![img](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)
>
>**Example:**
>
>```
>Input: "23"
>Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
>```
>**Note:**
>Although the above answer is in lexicographical order, your answer could be in any order you want.

## Solution

```cpp
// 25/02/2020
vector<string> letterCombinations(string digits) {
    std::vector<string> nums{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}; 
    vector<string> r;
    for (auto d: digits){
        if (r.empty()){
            for (char c: nums[d-'2']){
                r.push_back(string(1, c));
            }
        }
        else {
            vector<string> tmp;
            for (const auto &s: r){
                for (char c: nums[d-'2']){
                    string str(s);
                    str.push_back(c);
                    tmp.push_back(str);
                }
            }
            r = tmp;
        }
    }
    return r;
}
```