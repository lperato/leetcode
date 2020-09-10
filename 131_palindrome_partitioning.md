# 131 - Palindrome Partitioning

[leetcode link](https://leetcode.com/problems/palindrome-partitioning/)

> Given a string *s*, partition *s* such that every substring of the partition is a palindrome.
>
> Return all possible palindrome partitioning of *s*.
>
> **Example:**
>
> ```
> Input: "aab"
> Output:
> [
>   ["aa","b"],
>   ["a","a","b"]
> ]
> ```

## Backtracking + memo

```cpp
vector<vector<string>> partition(string s) {
    if(s.empty()) return {};
    Memo memo(s.size(), vector<char>(s.size(), -1));
    Result result; 
    Partition part;
    palindrome_partition_bt(result, memo, s, part);
    return result;
}

void palindrome_partition_bt(Result& result, Memo& memo, const string& s, Partition& part, int i=0){
    if(i == s.size()){
        result.push_back(part);
        return;
    }
    for(int j = i; j != s.size(); ++j){
        if(i == j || is_palindrome(memo, s, i, j)){
            part.push_back(s.substr(i, j-i+1));
            palindrome_partition_bt(result, memo, s, part, j+1);
            part.pop_back();
        }
    }
}

bool is_palindrome(Memo& memo, const string& s, int i, int j){
    if(memo[i][j] == -1){
        while(i<j && s[i] == s[j]){++i; --j;}
        memo[i][j] = i>=j;
    }
    return memo[i][j];
}
```
## 



