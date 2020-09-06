# 240 - Search a 2D Matrix II

[leetcode link](https://leetcode.com/problems/search-a-2d-matrix-ii/)

> Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:
>
> - Integers in each row are sorted in ascending from left to right.
> - Integers in each column are sorted in ascending from top to bottom.
>
> **Example:**
>
> Consider the following matrix:
>
> ```
> [
>   [1,   4,  7, 11, 15],
>   [2,   5,  8, 12, 19],
>   [3,   6,  9, 16, 22],
>   [10, 13, 14, 17, 24],
>   [18, 21, 23, 26, 30]
> ]
> ```
>
> Given target = `5`, return `true`.
>
> Given target = `20`, return `false`.

## Solution 1:  walk to target from last row and first column - O(M+N) 

```cpp
// 08/08/2020 - O(M+N)
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if(matrix.empty()) return false;
    for(int x = 0, y = matrix.size()-1, w = matrix[0].size(); y >=0 && x < w;){
        if(matrix[y][x] == target) return true;
        else if(matrix[y][x] > target) --y;
        else ++x;
    }
    return false;
}
```
## Solution 2 : recursive version of solution 1 - O(M+N)

```cpp
// 06/09/2020 - O(M+N) - recursive version
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    return !matrix.empty() && search_matrix(matrix, target, matrix.size()-1, 0);
}

bool search_matrix(vector<vector<int>> &matrix, int target, int row, int col){
    if (row == -1 || col == matrix[0].size()) return false;
    bool smaller = matrix[row][col] < target;
    return (matrix[row][col] == target) 
        || search_matrix(matrix, target, row-!smaller, col+smaller);
}
```
## Solution 3 : 2D binary search (wrong approach) - O(log(M)*log(N))?

```cpp
// 04/05/2020 - bad idea
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if(matrix.empty() || matrix[0].empty()) return false;
    return search_matrix(matrix, target, 0, 0, matrix[0].size()-1, matrix.size()-1);
}

bool search_matrix(vector<vector<int>>& matrix, int target, int x1, int y1, int x2, int y2){
    if (x1>x2 || y1 > y2) return false;
    if (x1 == x2 && y1 == y2) return matrix[y1][x1] == target;
    int mid_x = x1 + (x2 - x1) / 2;
    int mid_y = y1 + (y2 - y1) / 2;
    int midval = matrix[mid_y][mid_x];
    if (midval == target)
        return true;
    if (midval < target)
        return search_matrix(matrix, target, mid_x+1, y1, x2, mid_y)
            || search_matrix(matrix, target, x1, mid_y+1, mid_x, y2)
            || search_matrix(matrix, target, mid_x+1, mid_y+1, x2, y2);
    return search_matrix(matrix, target, mid_x+1, y1, x2, mid_y)
        || search_matrix(matrix, target, x1, mid_y+1, mid_x, y2)
        || search_matrix(matrix, target, x1, y1, mid_x, mid_y);
}
```
