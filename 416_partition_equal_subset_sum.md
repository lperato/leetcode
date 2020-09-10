# 416 - Partition Equal Subset Sum

[leetcode link](https://leetcode.com/problems/partition-equal-subset-sum/)

> Given a **non-empty** array containing **only positive integers**, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
>
> **Note:**
>
> 1. Each of the array element will not exceed 100.
> 2. The array size will not exceed 200.
>
> **Example 1:**
>
> ```
> Input: [1, 5, 11, 5]
> 
> Output: true
> 
> Explanation: The array can be partitioned as [1, 5, 5] and [11].
> ```
>
> **Example 2:**
>
> ```
> Input: [1, 2, 3, 5]
> 
> Output: false
> 
> Explanation: The array cannot be partitioned into equal sum subsets.
> ```

## Solution 1: Naïve recursion : TLE

```cpp
// 10/09/2020
bool canPartition(vector<int>& nums) {
    return can_partition(nums);
}

bool can_partition(const vector<int>& nums, int i = 0, int s1 = 0, int s2 = 0){
    if(i == nums.size()) return s1 == s2;
    return can_partition(nums, i+1, s1+nums[i], s2)
        || can_partition(nums, i+1, s1, s2 + nums[i]);
}
```
## Solution 2: Recursion with only 2 variables: TLE 

```cpp
// 10/09/2020
bool canPartition(vector<int>& nums) {
    int s = accumulate(nums.begin(), nums.end(), 0);
    if(s%2) return false;
    return can_partition(nums, s);
}

bool can_partition(const vector<int>& nums, int total, int i = 0, int s = 0){
    if(i >= nums.size()) return s == total/2;
    if(s > total/2) return false;
    return can_partition(nums, total, i+1, s+nums[i])
        || can_partition(nums, total, i+2, s);
}
```
## Solution 3: Recursion + memoization using `vector<vector<char>>`

```cpp
// 10/09/2020
// recursion with only 2 variables + pruning + memoization
// 1 - Each of the array element will not exceed 100.
// 2 - The array size will not exceed 200.
// 1 & 2 ==> maxsum = 20000
using Memo = vector<vector<char>>;
bool canPartition(vector<int>& nums) {
    int s = accumulate(nums.begin(), nums.end(), 0);
    if(s%2) return false;
    Memo memo(nums.size(), vector<char>(10001, -1));
    return can_partition(nums, memo, s);
}

bool can_partition(const vector<int>& nums, Memo& memo, int total, int i = 0, int s = 0){
    if(s > total/2) return false;
    if(i >= nums.size()) return s == total/2;
    if(memo[i][s] == -1){
        memo[i][s] = can_partition(nums, memo, total, i+1, s+nums[i]) 
                  || can_partition(nums, memo, total, i+2, s);
    }
    return memo[i][s];
}
```
## Solution 4: Recursion + memoization using `vector<unordered_map<int, bool>>`

```cpp
// 10/09/2020
// recursion + memo using vector<unrodered_map<int, char> as memo
using Memo = vector<unordered_map<int, bool>>;
bool canPartition(vector<int>& nums) {
    int s = accumulate(nums.begin(), nums.end(), 0);
    if(s%2) return false;
    Memo memo(nums.size());
    return can_partition(nums, memo, s);
}

bool can_partition(const vector<int>& nums, Memo& memo, int total, int i = 0, int s = 0){
    if(s > total/2) return false;
    if(i >= nums.size()) return s == total/2;
    if(auto it = memo[i].find(s); it == memo[i].end()){
        memo[i][s] = can_partition(nums, memo, total, i+1, s+nums[i]) 
                  || can_partition(nums, memo, total, i+2, s);
    }
    return memo[i][s];
}
```
## Other solutions that TLE

```cpp
// 19/08/2020
// dp set - TLE
bool canPartition(vector<int>& nums) {
    set<pair<int, int>> dp;
    vector<int> total_remaining(nums.size());
    for(int i = nums.size()-1; i>=0; --i)
        total_remaining[i] = ((i!= nums.size()-1)?total_remaining[i+1]:0) + nums[i];
    dp.emplace(nums[0], 0);
    for(int i = 1, size = nums.size(); i != size; ++i){
        set<pair<int, int>> tmp;
        for(auto [s1, s2]:dp){
            if(s2 + total_remaining[i] >= s1 + 2*nums[i])
                tmp.emplace(s1 + nums[i], s2);
            if(s1 + total_remaining[i] >= s2 + 2*nums[i])
                tmp.emplace(s1 , s2 + nums[i]);
        }
        dp = move(tmp);
    }
    return !dp.empty() 
        && any_of(dp.begin(), dp.end(), 
                  [](const pair<int,int >& a){return a.first == a.second;});
}
```