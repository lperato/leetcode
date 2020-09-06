# 835 - Image Overlap

[leetcode link](https://leetcode.com/problems/image-overlap/)

> Two images `A` and `B` are given, represented as binary, square matrices of the same size. (A binary matrix has only 0s and 1s as values.)
>
> We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the *overlap* of this translation is the number of positions that have a 1 in both images.
>
> (Note also that a translation does **not** include any kind of rotation.)
>
> What is the largest possible overlap?
>
> **Example 1:**
>
> ```
> Input: A = [[1,1,0],
>             [0,1,0],
>             [0,1,0]]
>        B = [[0,0,0],
>             [0,1,1],
>             [0,0,1]]
> Output: 3
> Explanation: We slide A to right by 1 unit and down by 1 unit.
> ```
>
> **Notes:** 
>
> 1. `1 <= A.length = A[0].length = B.length = B[0].length <= 30`
> 2. `0 <= A[i][j], B[i][j] <= 1`

# Solution 1 : Brute force O(n^4)

```cpp
// 06/09/2020
int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
    int max_overlap = 0;
    for(int ty = 0, s = A.size(); ty != s; ++ty){
        for(int tx = 0; tx != s; ++tx){
            max_overlap=max(max_overlap, overlap(A, B, tx, ty));
            max_overlap=max(max_overlap, overlap(B, A, tx, ty));
        }
    }
    return max_overlap;
}

int overlap(const vector<vector<int>>& A, const vector<vector<int>>& B, int tx, int ty){
    int overlap = 0;
    for(int y = ty, s = A.size(); y != s; ++y)
        for(int x = tx; x != s; ++x)
            overlap += (A[y-ty][x-tx] && B[y][x]);
    return overlap;
}
```