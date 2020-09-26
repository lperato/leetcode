# 278 - First Bad Version

[leetcode link](https://leetcode.com/problems/first-bad-version/)

> You are a  product manager and currently leading a team to develop a new product.  Unfortunately, the latest version of your product fails the quality  check. Since each version is developed based on the previous version,  all the versions after a bad version are also bad.
>
> Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.
>
> You are given an API `bool isBadVersion(version)` which will return whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
>
> **Example:**
>
> ```
> Given n = 5, and version = 4 is the first bad version.
> 
> call isBadVersion(3) -> false
> call isBadVersion(5) -> true
> call isBadVersion(4) -> true
> 
> Then 4 is the first bad version. 
> ```


## Solution 1 : Recursive binary search

```cpp
// 01/05/2020
int firstBadVersion(int n) {
    return bad_version(1, n);
}

int bad_version(int start, int end){
    if(start == end) return start;
    int mid = start + (end - start)/2;
    if(isBadVersion(mid))
        return bad_version(start, mid);
    return bad_version(mid+1, end);
}
```
### Shorter variant

```cpp
// 01/05/2020
int firstBadVersion(int n, int start = 1) {
    if(start == n) return start;
    int mid = start + (n - start)/2;
    if(isBadVersion(mid))
        return firstBadVersion(mid, start);
    return firstBadVersion(n, mid+1);
}
```
