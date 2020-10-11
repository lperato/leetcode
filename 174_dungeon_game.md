# 174 - Dungeon Game

[leetcode link](https://leetcode.com/problems/dungeon-game/)

> The demons had captured the princess (**P**) and  imprisoned her in the bottom-right corner of a dungeon. The dungeon  consists of M x N rooms laid out in a 2D grid. Our valiant knight (**K**) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
>
> The knight has an initial health point represented by a positive  integer. If at any point his health point drops to 0 or below, he dies  immediately.
>
> Some of the rooms are guarded by demons, so the knight loses health (*negative* integers) upon entering these rooms; other rooms are either empty (*0's*) or contain magic orbs that increase the knight's health (*positive* integers).
>
> In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
>
> **Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.**
>
> For example, given the dungeon below, the initial health of the knight must be at least **7** if he follows the optimal path `RIGHT-> RIGHT -> DOWN -> DOWN`.
>
> | -2 (K) | -3   |   3    |
> | ------ | ---- | :----: |
> | -5     | -10  |   1    |
> | 10     | 30   | -5 (P) |
>
> **Note:**
>
> - The knight's health has no upper bound.
> - Any room can contain threats or power-ups, even the first room the  knight enters and the bottom-right room where the princess is  imprisoned.

## Solution - DP

```cpp
// 22/06/2020
int calculateMinimumHP(vector<vector<int>>& dungeon) {
    auto h = dungeon.size();
    auto w = dungeon[0].size();
    vector<vector<int>> min_hp(h+1, vector<int>(w+1, numeric_limits<int>::max()));
    min_hp[h][w-1] = 1; min_hp[h-1][w] = 1;
    for(int j=h-1; j>=0; --j){
        for(int i=w-1; i>=0; --i){
            min_hp[j][i] = max(min(min_hp[j+1][i], min_hp[j][i+1]) - dungeon[j][i], 1);
        }
    }
    return min_hp[0][0];
}
```