# 27 - Remove Element

[leetcode link](https://leetcode.com/problems/remove-element/)

> Given an array *nums* and a value *val*, remove all instances of that value [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) and return the new length.
>
> Do not allocate extra space for another array, you must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.
>
> The order of elements can be changed. It doesn't matter what you leave beyond the new length.

## Solution 1 : Know your STL

```cpp
// 16/05/2020
int removeElement(vector<int>& nums, int val) {
    nums.erase(remove(nums.begin(), nums.end(), val), nums.end());
    return nums.size();
}
```
## Solution 2 : reinvent the wheel (badly)

```cpp
// 08/08/2020
int removeElement(vector<int>& nums, int val) {
    int removed = 0;
    for(int i=0, size = nums.size(); i+removed < size;){
        if(nums[i+removed] == val) {
            ++removed;
        }else {
            if(removed) nums[i] = nums[i+removed]; 
            ++i;
        }
    }
    return nums.size()-removed;
}
```
## Solution 3 : Reinvent the wheel (even more badly)

```cpp
// 16/05/2020
int removeElement(vector<int>& nums, int val) {
    int i;
    auto size = nums.size();
    for (i=0; i<size && nums[i]!=val; ++i);
    int nb_removed = i==size?0:1;
    while(i < size-nb_removed){
        if(nums[i+nb_removed] == val){
            nb_removed++;
        }else{
            nums[i] = nums[i+nb_removed];
            i++;
        }
    }
    return size-nb_removed;
}
```