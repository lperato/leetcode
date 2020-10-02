# 399 - Evaluate Division

[leetcode link](https://leetcode.com/problems/evaluate-division/)

> You are given `equations` in the format `A / B = k`, where `A` and `B` are variables represented as strings, and `k` is a real number (floating-point number). Given some `queries`, return *the answers*. If the answer does not exist, return `-1.0`.
>
> The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
>
> **Example 1:**
>
> ```
> Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
> Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
> Explanation: 
> Given: a / b = 2.0, b / c = 3.0
> queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
> return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
> ```
>
> **Example 2:**
>
> ```
> Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
> Output: [3.75000,0.40000,5.00000,0.20000]
> ```
>
> **Example 3:**
>
> ```
> Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
> Output: [0.50000,2.00000,-1.00000,-1.00000]
> ```
>
> **Constraints:**
>
> - `1 <= equations.length <= 20`
> - `equations[i].length == 2`
> - `1 <= equations[i][0].length, equations[i][1].length <= 5`
> - `values.length == equations.length`
> - `0.0 < values[i] <= 20.0`
> - `1 <= queries.length <= 20`
> - `queries[i].length == 2`
> - `1 <= queries[i][0].length, queries[i][1].length <= 5`
> - `equations[i][0], equations[i][1], queries[i][0], queries[i][1]` consist of lower case English letters and digits.

## Graph + DFS search solution

```cpp
// 27/09/2020
using Graph = unordered_map<string_view, vector<pair<string_view, double>>>;
using Visit = unordered_set<string_view>;
vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
    Graph adj;
    for(int i = 0, size = equations.size(); i!= size; ++i){
        adj[equations[i][0]].emplace_back(equations[i][1], values[i]);
        adj[equations[i][1]].emplace_back(equations[i][0], 1.0/values[i]);
    }
    vector<double> result;
    Visit visited;
    for(const auto& q: queries)
        result.push_back(dfs_search(adj, visited, q[0], q[1]));
    return result;
}

double dfs_search(const Graph& adj, Visit& visited, const string_view& s, const string& d){
    auto it = adj.find(s);
    if(it == adj.end())
        return -1;
    if(s == d)
        return 1;
    double res = -1;
    visited.insert(s);
    for(const auto& [a, v] : it->second){
        if(auto it1 = visited.find(a); it1 == visited.end()){
            if(double val = dfs_search(adj, visited, a, d); val != -1){
                res = val * v;
                break;
            }
        }  
    }
    visited.erase(s);
    return res;
}
```