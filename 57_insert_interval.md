# 57 - Insert Interval

[leetcode link](https://leetcode.com/problems/insert-interval/)

> Given a set of *non-overlapping* intervals, insert a new interval into the intervals (merge if necessary).
>
> You may assume that the intervals were initially sorted according to their start times.
>
> **Example 1:**
>
> ```
> Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
> Output: [[1,5],[6,9]]
> ```
>
> **Example 2:**
>
> ```
> Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
> Output: [[1,2],[3,10],[12,16]]
> Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
> ```
>
> **NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

## Over-complicated solution using `std::lower_bound` (inplace)

```cpp
// inplace
vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    if(intervals.empty())
        intervals.push_back(newInterval);
    else {
        auto it = lower_bound(intervals.begin(), intervals.end(), newInterval);
        if(it == intervals.end()){
            if(overlap(intervals.back(), newInterval))
                merge(intervals.back(), newInterval);
            else
                intervals.push_back(newInterval);
        } else {
            auto first_overlap = intervals.end();
            if(it != intervals.begin() && overlap(*prev(it), newInterval))
                first_overlap = prev(it);
            else if(overlap(*it, newInterval))
                first_overlap = it;
            if(first_overlap == intervals.end())
                intervals.insert(it, newInterval);
            else {
                merge(*first_overlap, newInterval);
                auto last = first_overlap+1;
                while(last != intervals.end() && overlap(*first_overlap, *last))
                    merge(*first_overlap, *last++);
                intervals.erase(first_overlap+1, last);
            }
        }
    }
    return intervals;
}

bool overlap(const vector<int>& a, const vector<int> &b){
    return (a[0] >= b[0] && a[0] <= b[1])
        || (a[1] >= b[0] && a[1] <= b[1])
        || (b[0] >= a[0] && b[0] <= a[1]);
}

void merge(vector<int>& a, const vector<int>& b){
    a[0] = min(a[0], b[0]);
    a[1] = max(a[1], b[1]);
}
```