# 452 - Minimum Number of Arrows to Burst Balloons

[leetcode link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

> There are some spherical balloons spread in two-dimensional space. For each balloon,  provided input is the start and end coordinates of the horizontal  diameter. Since it's horizontal, y-coordinates don't matter, and hence  the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.
>
> An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with `xstart` and `xend` bursts by an arrow shot at `x` if `xstart ≤ x ≤ xend`. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.
>
> Given an array `points` where `points[i] = [xstart, xend]`, return *the minimum number of arrows that must be shot to burst all balloons*.
>
> **Example 1:**
>
> ```
> Input: points = [[10,16],[2,8],[1,6],[7,12]]
> Output: 2
> Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
> ```
>
> **Example 2:**
>
> ```
> Input: points = [[1,2],[3,4],[5,6],[7,8]]
> Output: 4
> ```
>
> **Example 3:**
>
> ```
> Input: points = [[1,2],[2,3],[3,4],[4,5]]
> Output: 2
> ```
>
> **Example 4:**
>
> ```
> Input: points = [[1,2]]
> Output: 1
> ```
>
> **Example 5:**
>
> ```
> Input: points = [[2,3],[2,3]]
> Output: 1
> ```
>
> **Constraints:**
>
> - `0 <= points.length <= 104`
> - `points.length == 2`
> - `-231 <= xstart < xend <= 231 - 1`

## Solution 1: Sort intervals by left bound

This was my first idea, and not the most convenient for the problem, but still works:

```cpp
int findMinArrowShots(vector<vector<int>>& points) {
	sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b){
		return a[0]==b[0]?a[1]<b[1]:a[0]<b[0];});
	int n=0;
	for(int i = 0, size = points.size(), r; i != size; ++i){
		if(i == 0 || points[i][0] > r){
			++n;
			r = points[i][1];
		}else
			r = min(r, points[i][1]);
	}
	return n;
}
```

## Solution 2: Sort intervals by right bound

The problem can be solved in a more elegant fashion this way:

```cpp
int findMinArrowShots(vector<vector<int>>& points) {
	sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b){return a[1]<b[1];});
	int n=0;
	for(int i = 0, size = points.size(), r; i != size; ++i){
		if(i ==0 || points[i][0] > r){
			++n;
			r = points[i][1];
		} 
	}
	return n;
}
```

## Solution 3: same as solution 2 with accumulate

Short but not great, it obfuscates a bit the code

```cpp
int findMinArrowShots(vector<vector<int>>& points) {
	sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b){return a[1]<b[1];});
	int r;
	return accumulate(points.begin(), points.end(), 0, [&r](const int a, const vector<int>& b){
	   if(a == 0 || b[0] > r) {r = b[1]; return a+1;} else return a; });
}
```