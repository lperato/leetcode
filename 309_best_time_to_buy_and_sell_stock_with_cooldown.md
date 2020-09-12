# 309 - Best Time to Buy and Sell Stock with Cooldown

[leetcode link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

> Say you have an array for which the *i*th element is the price of a given stock on day *i*.
>
> Design an algorithm to find the maximum profit. You may complete as  many transactions as you like (ie, buy one and sell one share of the  stock multiple times) with the following restrictions:
>
> - You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
> - After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
>
> **Example:**
>
> ```
> Input: [1,2,3,0,2]
> Output: 3 
> Explanation: transactions = [buy, sell, cooldown, buy, sell]
> ```

## Recursion - TLE

```cpp
// 12/09/2020
// recursion without memo - TLE
int maxProfit(vector<int>& prices) {
    if(prices.empty()) return 0;
    return max_profit(prices);
}

int max_profit(vector<int>& prices, int i = 0, bool can_sell = false){
    if(i >= prices.size()) return can_sell?prices.back():0;
    if(can_sell)
        return max(
            max_profit(prices, i+2, false) + prices[i], // sell now
            max_profit(prices, i+1, true));             // sell later
    else
        return max(
            max_profit(prices, i+1, true) -prices[i],  // buy now
            max_profit(prices, i+1, false));           // buy later
}
```
## Recursion + memoization

```cpp
// 12/09/2020
// recursion without + memo
int maxProfit(vector<int>& prices) {
    if(prices.empty()) return 0;
    vector<vector<int>> memo(2, vector<int>(prices.size(), -1));
    return max_profit(prices, memo);
}

int max_profit(vector<int>& prices, vector<vector<int>>& memo, int i = 0, bool can_sell = false){
    if(i >= prices.size()) return can_sell?prices.back():0;
    if(memo[can_sell][i] == -1){
    if(can_sell)
        memo[can_sell][i] = max(
            max_profit(prices, memo, i+2, false) + prices[i], // sell now
            max_profit(prices, memo, i+1, true));             // sell later
    else
        memo[can_sell][i] = max(
            max_profit(prices, memo, i+1, true) -prices[i],  // buy now
            max_profit(prices, memo, i+1, false));           // buy later
    }
    return memo[can_sell][i];
}
```
