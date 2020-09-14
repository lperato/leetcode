# 714 - Best Time to Buy and Sell Stock with Transaction Fee

[leetcode link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

> Your are given an array of integers `prices`, for which the `i`-th element is the price of a given stock on day `i`; and a non-negative integer `fee` representing a transaction fee.
>
> You may complete as many transactions as you like, but you need to  pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before  you buy again.)
>
> Return the maximum profit you can make.
>
> **Example 1:**
>
> ```
> Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
> Output: 8
> Explanation: The maximum profit can be achieved by:
> Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling at prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
> ```
>
> **Note:**
>
> `0 < prices.length <= 50000`.
>
> `0 < prices[i] < 50000`.
>
> `0 <= fee < 50000`.

## Recursion + memoization (slow)

```cpp
// 12/09/2020
int maxProfit(vector<int>& prices, int fee) {
    vector<vector<int>> memo(2, vector<int>(prices.size(), -1));
    return max_profit(prices, memo, fee);
}

int max_profit(const vector<int>& prices, vector<vector<int>>& memo, int fee, int i=0, bool can_sell=false){
    if(i >= prices.size()-1) return can_sell?prices.back()-fee:0;
    if(memo[can_sell][i] == -1){
        memo[can_sell][i] = can_sell?
            max(max_profit(prices, memo, fee, i+1, false) + prices[i] - fee,   // sell now
                max_profit(prices, memo, fee, i+1, true))                // sell later
           :max(max_profit(prices, memo, fee, i+1, true) - prices[i],    // buy now
                max_profit(prices, memo, fee, i+1, false));              // buy later
    }
    return memo[can_sell][i];
}
```