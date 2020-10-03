# 128 - Longest Consecutive Sequence

[leetcode link](https://leetcode.com/problems/longest-consecutive-sequence/)

> Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
>
> Your algorithm should run in O(*n*) complexity.
>
> **Example:**
>
> ```
> Input: [100, 4, 200, 1, 3, 2]
> Output: 4
> Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
> ```

## Solution - O(n)

```cpp
int longestConsecutive(vector<int>& nums) {
    if(nums.empty()) return 0;
    unordered_map<int, int> seen;
    for(int i = 0, size = nums.size(); i != size; ++i) 
        seen[nums[i]] = i;
    vector<bool> visited(nums.size());
    int maxlen = 1;
    for(int i = 0, size = nums.size(); i != size; ++i) {
        if(!visited[i]){
            visited[i] = true;
            visited[seen[nums[i]]] = true;
            int j = 1;
            while(seen.find(nums[i]+j) != seen.end() && !visited[seen[nums[i]+j]]){
                visited[seen[nums[i]+j]] = true;
                ++j;
            }
            int k = 1;
            while(seen.find(nums[i]-k) != seen.end() && !visited[seen[nums[i]-k]]){
                visited[seen[nums[i]-k]] = true;
                ++k;
            }
            maxlen = max(maxlen, j+k-1);
        }
    }
    return maxlen;
}
```