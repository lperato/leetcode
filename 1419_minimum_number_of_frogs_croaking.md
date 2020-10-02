# 1419 - Minimum Number of Frogs Croaking

[leetcode lnk](https://leetcode.com/problems/minimum-number-of-frogs-croaking/)

> Given the string `croakOfFrogs`, which represents a combination of the string "croak" from different  frogs, that is, multiple frogs can croak at the same time, so multiple  “croak” are mixed. *Return the minimum number of* different *frogs to finish all the croak in the given string.*
>
> A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ **sequentially**. The frogs have to print all five letters to finish a croak. If the given  string is not a combination of valid "croak" return -1.
>
> **Example 1:**
>
> ```
> Input: croakOfFrogs = "croakcroak"
> Output: 1 
> Explanation: One frog yelling "croak" twice.
> ```
>
> **Example 2:**
>
> ```
> Input: croakOfFrogs = "crcoakroak"
> Output: 2 
> Explanation: The minimum number of frogs is two. 
> The first frog could yell "crcoakroak".
> The second frog could yell later "crcoakroak".
> ```
>
> **Example 3:**
>
> ```
> Input: croakOfFrogs = "croakcrook"
> Output: -1
> Explanation: The given string is an invalid combination of "croak" from different frogs.
> ```
>
> **Example 4:**
>
> ```
> Input: croakOfFrogs = "croakcroa"
> Output: -1
> ```
>
> **Constraints:**
>
> - `1 <= croakOfFrogs.length <= 10^5`
> - All characters in the string are: `'c'`, `'r'`, `'o'`, `'a'` or `'k'`.

## Solution 

```cpp
// 28/09/2020
int minNumberOfFrogs(string croakOfFrogs) {
    unordered_map<char, char> letter_pos;
    unordered_map<char, int> letter_count;
    string croak("croak");
    for(int i = 0; i < croak.size(); ++i)
        letter_pos[croak[i]] = i;
    
    int minfrogs = 0;
    int started = 0;
    for(auto c: croakOfFrogs){
        if(auto it = letter_pos.find(c); it == letter_pos.end())
            return -1;
        else{
            if(c == 'k')
                --started;
            else 
                ++letter_count[c];
            if(c == 'c')
                minfrogs = max(minfrogs, ++started);
            if(it->second != 0){
                auto &prev_letter_count = letter_count[croak[it->second - 1]];
                if(!prev_letter_count)
                    return -1;
                prev_letter_count--;
            }
        }
    }
    for(auto& [l, c]: letter_count)
        if(c != 0)
            return -1;
    return minfrogs;
}
```