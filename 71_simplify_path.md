# 71 - Simplify Path

[leetcode link](https://leetcode.com/problems/simplify-path/)

> Given an **absolute path** for a file (Unix-style), simplify it. Or in other words, convert it to the **canonical path**.
>
> In a UNIX-style file system, a period `.` refers to the current directory. Furthermore, a double period `..` moves the directory up a level.
>
> Note that the returned canonical path must always begin with a slash `/`, and there must be only a single slash `/` between two directory names. The last directory name (if it exists) **must not** end with a trailing `/`. Also, the canonical path must be the **shortest** string representing the absolute path.
>
> <removed examples>

## Solution

```cpp
// 12/08/2020
string simplifyPath(string path) {
    deque<string_view> dirs;
    for(int start = 0, pos = 0, end = path.size(); start < end;){
        pos = path.find('/', start);
        pos = (pos == string::npos?end:pos);
        if(pos-start == 2 && path.compare(start, pos-start, "..") == 0){
            if(!dirs.empty())
                dirs.pop_back();
        } else if (pos > start && (pos - start != 1 || path[start] != '.')){
            dirs.emplace_back(&path[start], pos-start);
        }
        start = pos+1;
    }
    string result;
    for(auto d: dirs){
        result.push_back('/');
        result.append(d);
    }
    return result.empty()?"/":result;
}
```