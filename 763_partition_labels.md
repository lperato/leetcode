# 763 - Partition Labels

[leetcode link](https://leetcode.com/problems/partition-labels/)

> A string `S` of lowercase English letters is given. We want  to partition this string into as many parts as possible so that each  letter appears in at most one part, and return a list of integers  representing the size of these parts.
>
> **Note:**
>
> - `S` will have length in range `[1, 500]`.
> - `S` will consist of lowercase English letters (`'a'` to `'z'`) only.

## O(n) time solution

```cpp
// 04/08/2020 
vector<int> partitionLabels(string S) {
    array<int, 'z'+1> lastpos{};
    for(int i = 0, sz = S.size(); i != sz; ++i)
        lastpos[S[i]] = i;
    vector<int> result(1, lastpos[S[0]]);
    for(int i = 1, sz = S.size(); i != sz; ++i){
        auto &last = result.back();
        if(i>last)
            result.push_back(lastpos[S[i]]);
        else
            last=max(last, lastpos[S[i]]);
    }
    for(int i = result.size()-1; i>0; --i)
        result[i] -= result[i-1];
    result[0]++;
    return result;
}
```