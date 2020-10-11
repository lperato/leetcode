# 187 - Repeated DNA Sequences

[leetcode link](https://leetcode.com/problems/repeated-dna-sequences/)

> All DNA is  composed of a series of nucleotides abbreviated as A, C, G, and T, for  example: "ACGAATTCCG". When studying DNA, it is sometimes useful to  identify repeated sequences within the DNA.
>
> Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
>
> **Example:**
>
> ```
> Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
> 
> Output: ["AAAAACCCCC", "CCCCCAAAAA"]
> ```

## Solution

```cpp
vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<string_view, int> seen;
    vector<string> result;
    for(int i = 0, j = s.size()-10; i <= j; ++i){
        auto view = string_view(&s[i], 10);
        auto &count = seen[view];
        if(count++ == 1)
            result.emplace_back(view);
    }
    return result;
}
```