# 188 - Best Time to Buy and Sell Stock IV

[leetcode link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

> Say you have an array for which the *i-*th element is the price of a given stock on day *i*.
>
> Design an algorithm to find the maximum profit. You may complete at most **k** transactions.
>
> **Note:**
>  You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
>
> **Example 1:**
>
> ```
> Input: [2,4,1], k = 2
> Output: 2
> Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
> ```
>
> **Example 2:**
>
> ```
> Input: [3,2,6,5,0,3], k = 2
> Output: 7
> Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
>              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
> ```

## Naive recursion : TLE

```cpp
// 12/09/2020
// naive recursive solution - TLE
int maxProfit(int k, vector<int>& prices) {
    if(prices.empty()) return 0;
    return max_profit(prices, k);      
}

int max_profit(vector<int>& prices, int k, int i=0, bool can_sell=false){
    if(k == 0 || i >= prices.size()-1) return (can_sell && k)?prices.back():0;
    return can_sell?
        max(max_profit(prices, k-1, i+1, false) + prices[i],   // sell now
            max_profit(prices, k, i+1, true))                  // sell later
       :max(max_profit(prices, k, i+1, true) - prices[i],      // buy now
            max_profit(prices, k, i+1, false));                // buy later
}
```
## Recursion + memoization + special case when K >= |prices| / 2

```cpp
// 12/09/2020
// recursion + memoization + optimiztion when k is irrelevant
using Memo = vector<vector<vector<int>>>;
int maxProfit(int k, vector<int>& prices) {
    if(prices.empty()) return 0;
    int maxprofit;
    if(k >= prices.size() / 2)
        maxprofit = max_profit(prices);
    else {
        Memo memo(2, vector<vector<int>>(k, vector<int>(prices.size(), -1)));
        maxprofit = max_profit(prices, memo, k);      
    }
    return maxprofit;
}

int max_profit(const vector<int>& prices, Memo& memo, int k, int i=0, bool can_sell=false){
    if(k == 0 || i >= prices.size()-1) return (can_sell && k)?prices.back():0;
    if(memo[can_sell][k-1][i] == -1){
        memo[can_sell][k-1][i] = can_sell?
            max(max_profit(prices, memo, k-1, i+1, false) + prices[i],   // sell now
                max_profit(prices, memo, k, i+1, true))                  // sell later
           :max(max_profit(prices, memo, k, i+1, true) - prices[i],      // buy now
                max_profit(prices, memo, k, i+1, false));                // buy later
    }
    return memo[can_sell][k-1][i];
}

int max_profit(vector<int>& prices) {
    int maxprofit = 0;
    for (int i = 1, size = prices.size(); i < size; ++i)
        maxprofit += max(0, prices[i] - prices[i - 1]);
    return maxprofit;
}
```