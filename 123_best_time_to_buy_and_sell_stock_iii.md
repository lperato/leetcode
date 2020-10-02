# 123 - Best Time to Buy and Sell Stock III

[leetcode link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

> Say you have an array for which the *i*th element is the price of a given stock on day *i*.
>
> Design an algorithm to find the maximum profit. You may complete at most *two* transactions.
>
> **Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
>
> **Example 1:**
>
> ```
> Input: prices = [3,3,5,0,0,3,1,4]
> Output: 6
> Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
> Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
> ```
>
> **Example 2:**
>
> ```
> Input: prices = [1,2,3,4,5]
> Output: 4
> Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
> Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
> ```
>
> **Example 3:**
>
> ```
> Input: prices = [7,6,4,3,1]
> Output: 0
> Explanation: In this case, no transaction is done, i.e. max profit = 0.
> ```
>
> **Example 4:**
>
> ```
> Input: prices = [1]
> Output: 0
> ```
>
> **Constraints:**
>
> - `1 <= prices.length <= 105`
> - `0 <= prices[i] <= 105`

## Solution 1

```cpp
// 11/08/2020
int maxProfit(vector<int>& prices) {
    auto size = prices.size();
    if(size < 2) return 0;
    
    vector<int> maxp(size, 0); // max profit from day 0 to i th day
    for(int i = 1, min_price = prices[0]; i != size; ++i){
        maxp[i] = max(maxp[i-1], prices[i]-min_price);
        min_price = min(prices[i], min_price);
    }
    
    vector<int> maxp_from(size, 0); // max profit from day i to last day
    for(int i = size-2, max_price = prices[size-1]; i >= 0; --i){
        maxp_from[i] = max(maxp_from[i+1], max_price - prices[i]);
        max_price = max(prices[i], max_price);
    }
    
    int max_profit = 0; // max profit for 2 transactions
    for(int i = 0; i != size; ++i){
        max_profit = max(max_profit, maxp[i] + maxp_from[i]);
    }
    return max_profit; 
}
```
## Gab's solution

```cpp
// Gab Solution
int maxProfit(const vector<int>& prices) {
    int sell1 = 0, sell2 = 0, buy1 = INT_MIN, buy2 = INT_MIN;
    for (const auto& price : prices) {
        buy1 = max(buy1, -price);
        sell1 = max(sell1, buy1 + price);
        buy2 = max(buy2, sell1 - price);
        sell2 = max(sell2, buy2 + price);
    }
    return sell2;        
}
```