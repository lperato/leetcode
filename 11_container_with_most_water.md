# 11 - Container With Most Water

[leetcode link](https://leetcode.com/problems/container-with-most-water/)

>Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
>Note: You may not slant the container and n is at least 2.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

## 2 pointers

```cpp
int maxArea(vector<int>& height) {
    int max_area = 0;
    for(auto p1 = height.begin(), p2 = prev(height.end()); p1 != p2; (*p1 > *p2)?--p2:++p1){
        int area = (p2 - p1) * min(*p1, *p2);
        max_area = max(max_area, area);
    }
    return max_area;
}
```

