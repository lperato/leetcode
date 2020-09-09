# 56 - Merge Intervals

[leetcode link](https://leetcode.com/problems/merge-intervals/)

> Given a collection of intervals, merge all overlapping intervals.
>
> **Example 1:**
>
> ```
> Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
> Output: [[1,6],[8,10],[15,18]]
> Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
> ```
>
> **Example 2:**
>
> ```
> Input: intervals = [[1,4],[4,5]]
> Output: [[1,5]]
> Explanation: Intervals [1,4] and [4,5] are considered overlapping.
> ```
>
> **NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
>
>  
>
> **Constraints:**
>
> - `intervals[i][0] <= intervals[i][1]`

## Solution

```cpp
// 04/03/2020
vector<vector<int>> merge(vector<vector<int>>& intervals) {
    if (intervals.size() == 0)
        return vector<vector<int>>();
    if (intervals.size() == 1)
        return intervals;
    std::sort(intervals.begin(), intervals.end());
    vector<vector<int>> res({intervals[0]});
    for (auto it = intervals.begin()+1; it != intervals.end(); ++it){
        if(overlap(*it, res.back())){
            res.back() = merge(*it, res.back());
        }else{
            res.push_back(*it);
        }
    }
    return res;
}

bool overlap(const vector<int>& i1, const vector<int>& i2){
    return (i1[0] >= i2[0] && i1[0] <= i2[1]) 
        || (i1[1] >= i2[0] && i1[1] <= i2[1])
        || (i2[0] >= i1[0] && i2[0] <= i1[1]);
}

vector<int> merge(const vector<int>& i1, const vector<int>& i2){
    return vector<int>{min(i1[0], i2[0]), max(i1[1], i2[1])};
}
```