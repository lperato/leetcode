# 658 - Find K Closest Elements

[leetcode link](https://leetcode.com/problems/find-k-closest-elements/)

> Given a sorted array `arr`, two integers `k` and `x`, find the `k` closest elements to `x` in the array. The result should also be sorted in ascending order. If  there is a tie, the smaller elements are always preferred.
>
> **Example 1:**
>
> ```
> Input: arr = [1,2,3,4,5], k = 4, x = 3
> Output: [1,2,3,4]
> ```
>
> **Example 2:**
>
> ```
> Input: arr = [1,2,3,4,5], k = 4, x = -1
> Output: [1,2,3,4]
> ```
>
> **Constraints:**
>
> - `1 <= k <= arr.length`
> - `1 <= arr.length <= 10^4`
> - Absolute value of elements in the array and `x` will not exceed 104

## Solution 1: nth_element

```cpp
// 22/09/2020
vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    if(k < arr.size())
        nth_element(arr.begin(), arr.begin()+k, arr.end(), 
                    [&x](int a, int b){int c = abs(a-x), d = abs(b-x); return c < d || c == d && a < b;});
    vector<int> result(arr.begin(), arr.begin()+k);
    sort(result.begin(), result.end());
    return result;
}
```
## Solution 2: partial_sort_copy

```cpp
// 03/08/2020 
vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    vector<int> k_closest(k);
    partial_sort_copy(arr.begin(), arr.end(), k_closest.begin(), k_closest.end(), 
                      [&x](int a, int b){int c = abs(a-x), d = abs(b-x); return c < d || (c==d && a < b);});
    sort(k_closest.begin(), k_closest.end());
    return k_closest;
```
