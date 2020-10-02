# 48 - Rotate Image

[leetcode link](https://leetcode.com/problems/rotate-image/)

> You are given an *n* x *n* 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).
>
> You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)
>
> ```
> Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
> Output: [[7,4,1],[8,5,2],[9,6,3]]
> ```
>
> **Example 2:**
>
> ![img](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)
>
> ```
> Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
> Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
> ```
>
> **Example 3:**
>
> ```
> Input: matrix = [[1]]
> Output: [[1]]
> ```
>
> **Example 4:**
>
> ```
> Input: matrix = [[1,2],[3,4]]
> Output: [[3,1],[4,2]]
> ```
>
> **Constraints:**
>
> - `matrix.length == n`
> - `matrix[i].length == n`
> - `1 <= n <= 20`
> - `-1000 <= matrix[i][j] <= 1000`

**TODO** Figure Gab's solution

## Solution 1 

```cpp
void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();
    int cx = n/2, cy = cx;
    for(int y=0; y<cy+n%2; ++y){
        for(int x=0; x<cx; ++x){
            int tmp = matrix[y][x];
            int x1 = x, y1 = y;
            for(int k = 0; k != 4; ++k){
                int rx = -y1+cx+cy-1+n%2;
                int ry = x1-cx+cy;
                if(rx == x1 && ry == y1)
                    break;
                swap(tmp, matrix[ry][rx]);
                x1=rx;
                y1=ry;
            }
        }
    }  
}
```
## Gab's solution

```cpp
void rotate(vector<vector<int>>& matrix) {
    for (int a = 0, b = matrix.size() - 1; a < b; ++a, --b) {
        for (int i = 0; i != b - a; ++i) {
            swap(matrix[a][a + i], matrix[a + i][b]);
            swap(matrix[a][a + i], matrix[b][b - i]);
            swap(matrix[a][a + i], matrix[b - i][a]);
        }
    }
}
```

