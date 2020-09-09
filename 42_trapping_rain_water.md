# 42 - Trapping Rain Water

[leetcode link]()

> Given *n* non-negative integers representing an elevation map where the width of  each bar is 1, compute how much water it is able to trap after raining.
>
> ![img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
>  The above elevation map is represented by array  [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue  section) are being trapped. **Thanks Marcos** for contributing this image!
>
> **Example:**
>
> ```
> Input: [0,1,0,2,1,0,1,3,2,1,2,1]
> Output: 6
> ```

## Solution

```cpp
22/02/2020
int trap(vector<int>& height) {
    int max = 0;
    int m = -1;
    for (int i = 0; i < height.size(); i++){
        if (height[i] > max){
            max = height[i];
            m = i;
        }
    }
    int w = 0;
    int h = 0;
    for (int i = 0; i < m; i++)
    {
        int y = height[i];
        if (y > h)
            h = y;
        else
            w += h-y;
    }
    h = 0;
    for (int i = height.size()-1; i > m; i--)
    {
        int y = height[i];
        if (y > h)
            h = y;
        else
            w += h-y;
    }
    return w;
}
```