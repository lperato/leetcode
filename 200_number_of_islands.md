# 200 - Number of Islands

[leetcode link](https://leetcode.com/problems/number-of-islands/)

> Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water  and is formed by connecting adjacent lands horizontally or vertically.  You may assume all four edges of the grid are all surrounded by water.
>
> **Example 1:**
>
> ```
> Input: grid = [
>   ["1","1","1","1","0"],
>   ["1","1","0","1","0"],
>   ["1","1","0","0","0"],
>   ["0","0","0","0","0"]
> ]
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: grid = [
>   ["1","1","0","0","0"],
>   ["1","1","0","0","0"],
>   ["0","0","1","0","0"],
>   ["0","0","0","1","1"]
> ]
> Output: 3
> ```

## Solution

```cpp
int numIslands(vector<vector<char>>& grid) {
    int nb_islands = 0;
    for(int y = 0; y < grid.size(); y++){
        for(int x = 0; x < grid[y].size(); x++){
            if(grid[y][x]=='1'){
                nb_islands++;
                flood_land(grid, x, y);
            }
        }
    }
    return nb_islands;
}

void flood_land(vector<vector<char>>& grid, int x, int y){
    grid[y][x] = '0';
    if(x!=0 && grid[y][x-1]=='1') flood_land(grid, x-1, y);
    if(x!=grid[y].size()-1 && grid[y][x+1]=='1') flood_land(grid, x+1, y);
    if(y!=0 && grid[y-1][x]=='1') flood_land(grid, x, y-1);
    if(y!=grid.size()-1 && grid[y+1][x]=='1') flood_land(grid, x, y+1);
}
```
