# 84 - Largest Rectangle in Histogram

[leetcode link](https://leetcode.com/problems/largest-rectangle-in-histogram/)

> Given *n* non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the  histogram.
>
> ![img](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)
>  Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.
>
> ![img](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)
>  The largest rectangle is shown in the shaded area, which has area = `10` unit.
>
> **Example:**
>
> ```
> Input: [2,1,5,6,2,3]
> Output: 10
> ```

## Recursive solution - very slow (TLE from time to time)

```cpp
int largestRectangleArea(vector<int>& heights) {
    return max_rectangle_area(heights.begin(), heights.end());
}

int max_rectangle_area(vector<int>::iterator begin, vector<int>::iterator end) {
    if (begin == end)
        return 0;
    if (begin == end - 1)
        return *begin;
    auto min_e = min_element(begin, end);
    return max({*min_e * (end-begin),
                max_rectangle_area(begin, min_e),
                max_rectangle_area(min_e+1, end)}); 
}
```