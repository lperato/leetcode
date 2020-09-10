# 165 - Compare Version Numbers

[leetcode link](https://leetcode.com/problems/compare-version-numbers/)

> Compare two version numbers *version1* and *version2*.
>  If `*version1* > *version2*` return `1;` if `*version1* < *version2*` return `-1;`otherwise return `0`.
>
> You may assume that the version strings are non-empty and contain only digits and the `.` character.
>
> The `.` character does not represent a decimal point and is used to separate number sequences.
>
> For instance, `2.5` is not "two and a half" or "half way  to version three", it is the fifth second-level revision of the second  first-level revision.
>
> You may assume the default revision number for each level of a version number to be `0`. For example, version number `3.4` has a revision number of `3` and `4` for its first and second level revision number. Its third and fourth level revision number are both `0`.
>
> ... <examples>
>
> **Note:**
>
> 1. Version strings are composed of numeric strings separated by dots `.` and this numeric strings **may** have leading zeroes. 
> 2. Version strings do not start or end with dots, and they will not be two consecutive dots.

## Recursive solutions

### Initial solution

```cpp
// 09/09/2020 - initial solution
int compareVersion(string version1, string version2) {
    return compare_version(version1, version2);   
}

int compare_version(const string& v1, const string& v2, int i=0, int j=0){
    if(i >= v1.size() && j >= v2.size()) return 0;
    int n1, n2, p1, p2;
    if(i >= v1.size()){
        p1 = i-1;
        n1 = 0;
    } else {
        p1 = min(v1.size(), v1.find('.', i));
        n1 = stoi(v1.substr(i, p1-i));
    }
    if(j >= v2.size()){
        p2 = j-1;
        n2 = 0;
    } else {
        p2 = min(v2.size(), v2.find('.', j));
        n2 = stoi(v2.substr(j, p2-j));
    }
    if(n1 > n2) return 1;
    else if(n1 < n2) return -1;
    else return compare_version(v1, v2, p1+1, p2+1);
}
```
### More compact solution with lambda

```cpp
// 09/09/2020 - slightly more compact solution
int compareVersion(string version1, string version2) {
    return compare_version(version1, version2);   
}

int compare_version(const string& v1, const string& v2, int i=0, int j=0){
    if(i >= v1.size() && j >= v2.size()) return 0;
    auto get_num = [](const string& s, int &pos) -> pair<int, int> {
        if(pos >= s.size()) return {0, pos};
        int p = min(s.size(), s.find('.', pos));
        return {stoi(s.substr(pos, p-pos)), p+1};
    };
    auto [n1, p1] = get_num(v1, i);
    auto [n2, p2] = get_num(v2, j);
    if(n1 > n2) return 1;
    else if(n1 < n2) return -1;
    else return compare_version(v1, v2, p1, p2);
} 
```

## Convert version string to vector then compare vectors (Gab's solution)

```cpp
int compareVersion(const string& version1, const string& version2) {
    auto vers1 = extract(version1), vers2 = extract(version2);
    return (vers1 == vers2) ? 0 : (vers1 < vers2) ? -1 : 1;
}

static vector<int> extract(const string& s) {
    istringstream iss(s);
    vector<int> vers;
    for (string v; getline(iss, v, '.'); vers.push_back(stoi(v)));
    for (; !vers.empty() && vers.back() == 0; vers.pop_back());
    return vers;
}
```
