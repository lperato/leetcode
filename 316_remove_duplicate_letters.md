# 316 - Remove Duplicate Letters

[leetcode link](https://leetcode.com/problems/remove-duplicate-letters/)

> Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.
>
> **Note:** This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
>
> **Example 1:**
>
> ```
> Input: s = "bcabc"
> Output: "abc"
> ```
>
> **Example 2:**
>
> ```
> Input: s = "cbacdcbc"
> Output: "acdb"
> ```
>
> **Constraints:**
>
> - `1 <= s.length <= 104`
> - `s` consists of lowercase English letters.

## Solution: use the result as a stack - O(n)

- keep track of remaining letter count in the input string (`lettercount` variable)
- keep track of each letter added to the result (`added` variable)
- iterate over the input string
  - if current letter should be before the last letter added to the result and if there is another occurence of that letter after
    - then remove the letter from the result
  - repeat until not possible
  - append the current letter to the result

```cpp
// 11/10/2020
string removeDuplicateLetters(string s) {
	array<int, 'z'+1> lettercount{};
	for(auto c: s)
		lettercount[c]++;
	array<bool, 'z'+1> added{};
	string result;
	for(auto c: s){
		lettercount[c]--;
		if(added[c]) 
			continue;
		while(!result.empty() && result.back() > c && lettercount[result.back()]>0){
			added[result.back()] = false;
			result.pop_back();
		}
		result.push_back(c);
		added[c] = true;
	}
	return result;
}
```