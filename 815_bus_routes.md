# 815 - Bus Routes

[leetcode link](https://leetcode.com/problems/bus-routes/)

> We have a list of bus routes. Each `routes[i]` is a bus route that the i-th bus repeats forever. For example if `routes[0] = [1, 5, 7]`, this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.
>
> We start at bus stop `S` (initially not on a bus), and we want to go to bus stop `T`. Travelling by buses only, what is the least number of buses we must  take to reach our destination? Return -1 if it is not possible.
>
> ```
> Example:
> Input: 
> routes = [[1, 2, 7], [3, 6, 7]]
> S = 1
> T = 6
> Output: 2
> Explanation: 
> The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
> ```
>
> **Constraints:**
>
> - `1 <= routes.length <= 500`.
> - `1 <= routes[i].length <= 10^5`.
> - `0 <= routes[i][j] < 10 ^ 6`.

## Solution : BFS on bus routes graph

### Approach : 

Reason about a graph of bus routes, not a graph of bus stations:

1. Transform the input data into an adjacency list of bus routes
   - sort the stations for each bus route (not needed, the problem description does not say it but the test data is)
   - compare all bus routes with each other, and detect adjacent bus routes by looking for a common station between 2 routes
   - add a sink node, and make it a neighbor of any bus route includes the target station
2. Apply BFS on the generated graph
   - initialize the BFS queue with all routes that includes the source station

```cpp
// 15/09/2020

bool sorted_array_intersect(const vector<int>& a, const vector<int>& b){
    if (a.back() < b.front() || b.back() < a.front())   // important optimisation!
        return false;
    for(int i=0, j=0, sa=a.size(), sb=b.size(); i != sa && j!=sb;) {
        if (a[i] == b[j]) return true;
        else if (a[i] < b[j]) ++i;
        else ++j;
    }
    return false;
}

int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
    if(S == T) return 0;    // obvious corner case
    deque<int> queue;
    vector<bool> visited(routes.size()+1);             // visited bus routes
    vector<vector<int>> adj_routes(routes.size()+1 );  // adjacency list of routes
    for(int i=0, size=routes.size(); i != size; ++i){
        for(int j=i+1; j != size; ++j)
            if(sorted_array_intersect(routes[i], routes[j])){
                adj_routes[i].push_back(j);
                adj_routes[j].push_back(i);
            }
        if(binary_search(routes[i].begin(), routes[i].end(), T))
            adj_routes[i].push_back(routes.size());
        if(binary_search(routes[i].begin(), routes[i].end(), S)){
            queue.push_back(i);
            visited[i] = true;
        }
    }
    int nbroutes = -1;
    while(!queue.empty()){
        ++nbroutes;
        for(int i=0, qsize=queue.size(); i != qsize; ++i){
            auto r = queue.front();
            queue.pop_front();
            if(r == routes.size())
                return nbroutes;
            for(auto ar: adj_routes[r]){
                if(!visited[ar]){
                    visited[ar] = true;
                    queue.push_back(ar);
                }
            }   
        }
    }
    return -1;
}
```