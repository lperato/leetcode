# 74 - Search a 2D Matrix

[leetcode link](https://leetcode.com/problems/search-a-2d-matrix/)

> Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:
>
> - Integers in each row are sorted from left to right.
> - The first integer of each row is greater than the last integer of the previous row.
>
> **Example 1:**
>
> ```
> Input:
> matrix = [
>   [1,   3,  5,  7],
>   [10, 11, 16, 20],
>   [23, 30, 34, 50]
> ]
> target = 3
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input:
> matrix = [
>   [1,   3,  5,  7],
>   [10, 11, 16, 20],
>   [23, 30, 34, 50]
> ]
> target = 13
> Output: false
> ```

## Solution - 2D binary search

```cpp
// 11/03/2020
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    return search_matrix(matrix.begin(), matrix.end(), target);
}

bool search_matrix( vector<vector<int>>::iterator begin, 
                    vector<vector<int>>::iterator end, 
                    int target){
    if (begin == end)
        return false;
    auto it = begin + (end - begin) / 2;
    vector<int>& v = *it;
    if (v.empty())
        return false;
    if (v.front() <= target && target <= v.back() ){
        return find(v.begin(), v.end(), target) != v.end();
    }
    else if (target < v.front()) {
        return search_matrix(begin, it, target);
    }
    else{
        return search_matrix(it+1, end, target);
    }
}
```