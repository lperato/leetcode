# 149 - Max Points on a Line

[leetcode link](https://leetcode.com/problems/max-points-on-a-line/)

> Given *n* points on a 2D plane, find the maximum number of points that lie on the same straight line.
>
> **Example 1:**
>
> ```
> Input: [[1,1],[2,2],[3,3]]
> Output: 3
> Explanation:
> ^
> |
> |        o
> |     o
> |  o  
> +------------->
> 0  1  2  3  4
> ```
>
> **Example 2:**
>
> ```
> Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
> Output: 4
> Explanation:
> ^
> |
> |  o
> |     o        o
> |        o
> |  o        o
> +------------------->
> 0  1  2  3  4  5  6
> ```
>
> **NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

## Solution

```cpp
// 08/04/2020
long to_long(const vector<int>& pt){
    return *(const long*)(const int*)(pt.data());
}

int maxPoints(vector<vector<int>>& points) {
    if(points.size() < 3)
        return points.size();
    int maxduplicate = 1;
    unordered_map<long, unsigned int> mpoints;
    for(const auto& p: points){
        auto it = mpoints.find(to_long(p));
        if (it != mpoints.end()){
            it->second++;
            maxduplicate = it->second>maxduplicate?it->second:maxduplicate;
        }else{
            mpoints[to_long(p)] = 1;
        }
    }
    
    if(mpoints.size() < 3){
        int sum = 0;
        for(const auto it: mpoints){
            sum += it.second;
        }
        return sum;
    }
    
    int maxpt = 2;
    for(auto p1=mpoints.cbegin(); p1 != mpoints.cend(); ++p1){
        for(auto p2 = next(p1); p2 != mpoints.cend(); ++p2){  
            int n = p1->second + p2->second;
            for(auto p3 = next(p2); p3 != mpoints.cend(); ++p3){
                n+= collinear((const int*)&(p1->first), (const int*)&(p2->first), (const int*)&(p3->first))?p3->second:0;
            }
            maxpt = n>maxpt?n:maxpt;
        } 
    }
    return max<int>(maxpt, 1+maxduplicate);
}

//bool collinear(const vector<int>& p1, const vector<int>& p2, const vector<int>& p3) {
bool collinear(const int * p1, const int *p2, const int* p3){
	return (long)(p1[1] - p2[1]) * (p1[0] - p3[0]) ==  (long)(p1[1] - p3[1]) * (p1[0] - p2[0]);
}
```