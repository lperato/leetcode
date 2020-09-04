# 1 - Two Sums

[leetcode link](https://leetcode.com/problems/two-sum/)

> Given an array of integers nums and and integer target, 
> return the indices of the two numbers such that they add up to target.
> You may assume that each input would have exactly one solution, 
> and you may not use the same element twice.
>
> You can return the answer in any order.

## Using unordered_map - 2 pass - O(n)

```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    std::unordered_map<int, int> m; 
    auto size = nums.size();
    for (size_t i = 0; i != size; i++)
        m[nums[i]] = i;
        
    for (int i = 0; i != size; i++){
        int target_j = target - nums[i];
        if (auto it = m.find(target_j); it != m.end()){
            auto j = it->second;
            if (i != j){
                return {i, j};
            }
        }
    }
    return {};
}
```

## Brute force - O(n^2)

```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    auto size = nums.size();
    for (int i = 0; i < size; i++){
        int target_j = target - nums[i];
        for (int j = 0; j < size; j++){
            if (i == j)
                continue;
            if (nums[j] == target_j)
                return {i, j};
        }
    }
    return vector<int>();
}
```