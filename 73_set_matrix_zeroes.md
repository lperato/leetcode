# 73 - Set Matrix Zeroes

[leetcode link](https://leetcode.com/problems/set-matrix-zeroes/)

> Given an `*m* x *n*` matrix. If an element is **0**, set its entire row and column to **0**. Do it [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm).
>
> **Follow up:**
>
> - A straight forward solution using O(*m**n*) space is probably a bad idea.
> - A simple improvement uses O(*m* + *n*) space, but still not the best solution.
> - Could you devise a constant space solution?
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)
>
> ```
> Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
> Output: [[1,0,1],[0,0,0],[1,0,1]]
> ```
>
> **Example 2:**
>
> ![img](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
>
> ```
> Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
> Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
> ```
>
> **Constraints:**
>
> - `m == matrix.length`
> - `n == matrix[0].length`
> - `1 <= m, n <= 200`
> - `-231 <= matrix[i][j] <= 231 - 1`

## Solution (Ugly) - O(1) space

```cpp
// 10/03/2020
void setZeroes(vector<vector<int>>& matrix) {
    if (matrix.empty())
        return;
    int bufferline = -1;
    int lastzero = 0;
    for (int j = 0; j < matrix.size(); j++){
        auto & line = matrix[j];
        bool has_zero = false;
        for (int i = 0; i < line.size(); i++){
            if (line[i] == 0){
                has_zero = true;
                if (bufferline == -1){
                    bufferline = j;
                }
                if (j == bufferline){
                    for(int k = lastzero; k < i; k++)
                        line[k] = 0; 
                    lastzero = i+1;
                }
                matrix[bufferline][i] = 1;
            }
        }
        if (j == bufferline){
            for(int k = lastzero; k < line.size(); k++)
                line[k] = 0; 
        }
        if (has_zero && bufferline != j){
            for(int k = 0; k < line.size(); k++)
                line[k] = 0;
        }
    }
    if (bufferline == -1)
        return;
    for (int col = 0; col < matrix[bufferline].size(); col++){
        if (matrix[bufferline][col] == 1){
            for(int j=0; j < matrix.size(); j++){
                matrix[j][col] = 0;
            }
        }
    }        
}
```
## Solution - O(n) space

```cpp
// 10/09/2020
void setZeroes(vector<vector<int>>& matrix) {
    if(matrix.empty()) return;
    vector<bool> zerocol(matrix[0].size());
    for(int r = 0, nrows = matrix.size(), ncols = matrix[0].size(); r != nrows; ++r){
        bool has_zero = false;
        for(int c = 0; c != ncols; ++c){
            if(matrix[r][c] == 0){
                zerocol[c] = true;
                has_zero = true;
            }
        }
        if(has_zero)
            for(auto &cell: matrix[r])
                cell = 0;
    }
    for(int c = 0, ncols = matrix[0].size(); c != ncols; ++c){
        if(zerocol[c])
            for(auto &row: matrix)
                row[c] = 0;
    }
}
```

## 