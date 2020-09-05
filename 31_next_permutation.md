# 31 - Next Permutation

[leetcode link](https://leetcode.com/problems/next-permutation/)

> Implement **next permutation**, which rearranges numbers into the lexicographically next greater permutation of numbers.
>
> If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
>
> The replacement must be **[in-place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory.
>
> Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
>
> ```
> 1,2,3` → `1,3,2`
>  `3,2,1` → `1,2,3`
>  `1,1,5` → `1,5,1
> ```

## Solution

```cpp
void nextPermutation(vector<int>& nums) {
    if (nums.size() < 2)
        return;
    auto it = nums.end()-1;
    for(; it!= nums.begin() && *(it-1) >= *it; --it);
    if(it != nums.begin()){
        auto min = it;
        for(auto it1 = min+1; it1 != nums.end(); ++it1){
            if (*it1 > *(it-1) && *it1 <= *min)
                min = it1;
        }
        swap(*(it-1), *min);
    }
    reverse(it, nums.end());
}
```