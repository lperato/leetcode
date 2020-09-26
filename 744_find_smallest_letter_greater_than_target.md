# 744 - Find Smallest Letter Greater Than Target

[leetcode link](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

> Given a list of sorted characters `letters` containing only lowercase letters, and given a target letter `target`, find the smallest element in the list that is larger than the given target.
>
> Letters also wrap around.  For example, if the target is `target = 'z'` and `letters = ['a', 'b']`, the answer is `'a'`.
>
> <skipped examples>
>
> **Note:**
>
> 1. `letters` has a length in range `[2, 10000]`.
> 2. `letters` consists of lowercase letters, and contains at least 2 unique letters.
> 3. `target` is a lowercase letter.

## Solution 1: linear scan - O(n)

```cpp
// 20/09/2020
// O(n) solution - naive scan of the array
char nextGreatestLetter(vector<char>& letters, char target) {
    char min_letter = 'z'+1;
    for(auto c: letters)
        if(c > target)
            min_letter = min(min_letter, c);
    return min_letter == 'z'+1?letters[0]:min_letter;
}
```
## Solution 2: binary search O(log(n))

```cpp
// 20/09/2020
// O(log(n)) solution - binary search
// letters are sorted -> binary search
char nextGreatestLetter(vector<char>& letters, char target) {
    int l = 0, r = letters.size();
    while(l < r){
        int mid = l + (r-l)/2;
        if(letters[mid] <= target)
            l = mid+1;
        else
           r = mid;  
    }
    return letters[l] <= target?letters[0]:letters[l];
}
```
