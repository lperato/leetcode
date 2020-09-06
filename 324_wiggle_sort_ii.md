# 324 - Wiggle Sort II

[leetcode link](https://leetcode.com/problems/wiggle-sort-ii/)

> Given an unsorted array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`.
>
> **Example 1:**
>
> ```
> Input: nums = [1, 5, 1, 1, 6, 4]
> Output: One possible answer is [1, 4, 1, 5, 1, 6].
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [1, 3, 2, 2, 3, 1]
> Output: One possible answer is [2, 3, 1, 3, 1, 2].
> ```
>
> **Note:**
>  You may assume all input has valid answer.
>
> **Follow Up:**
>  Can you do it in O(n) time and/or in-place with O(1) extra space?

## Solution 1 : sort then interleave both halves backward - O(nlog(n)) time, O(n) space

```cpp
// 06/09/2020
// time O(nlog(n)) - space O(n) 
void wiggleSort(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    std::vector<int> cp(nums.begin(), nums.end());
    for(int i =0, sz = nums.size(), l = (sz-1)/2, r = sz-1; i!= sz; ++i)
        nums[i] = (i%2)?cp[r--]:cp[l--]; 
}
```
## Solution 2: partition left, middle value, right then interleave both halves backward - O(n) time, O(n) space

```cpp
// 06/09/2020
// time O(n) - space O(n)
void wiggleSort(vector<int>& nums) {
    partition_left_middle_right(nums);
    std::vector<int> cp(nums.begin(), nums.end());
    for(int i =0, sz = nums.size(), l = (sz-1)/2, r = sz-1; i!= sz; ++i)
        nums[i] = (i%2)?cp[r--]:cp[l--]; 
}

using It = vector<int>::iterator;
pair<It, It> partition_left_middle_right(vector<int>& nums) {
    auto mid = nums.begin() + nums.size() / 2;
    nth_element(nums.begin(), mid, nums.end());
    auto right = mid;
    for(auto it = right; it != nums.end() && right != nums.end(); ++it)
        if(*it == *mid)
            iter_swap(it, right++);
    auto left = mid;
    while(*left == *mid && left != nums.begin())left--;
    for(auto it = nums.begin(); it < left; ++it)
        if(*it == *mid)
            iter_swap(it, left--);
    return {left, right};
}
```
**TODO** 

- Figure how to perform the swaps in place
- understand 3 way partitioning (https://en.wikipedia.org/wiki/Dutch_national_flag_problem)

## Interesting solutions

[O(n)+O(1) after median --- Virtual Indexing](https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing)

[3 lines Python, with Explanation / Proof](https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof)

[Step by step explanation of index mapping in Java](https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/Step-by-step-explanation-of-index-mapping-in-Java)

[O(n)-time O(1)-space solution with detail explanations](https://leetcode.com/problems/wiggle-sort-ii/discuss/77681/O(n)-time-O(1)-space-solution-with-detail-explanations)

[Summary of the various solutions to Wiggle Sort ](https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/Summary-of-the-various-solutions-to-Wiggle-Sort-for-your-reference)