# 122 - Best Time to Buy and Sell Stock II

[leetcode link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

> Say you have an array `prices` for which the *i*th element is the price of a given stock on day *i*.
>
> Design an algorithm to find the maximum profit. You may complete as  many transactions as you like (i.e., buy one and sell one share of the  stock multiple times).
>
> **Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
>
> **Example 1:**
>
> ```
> Input: [7,1,5,3,6,4]
> Output: 7
> Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
>              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
> ```
>
> **Example 2:**
>
> ```
> Input: [1,2,3,4,5]
> Output: 4
> Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
>              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
>              engaging multiple transactions at the same time. You must sell before buying again.
> ```
>
> **Example 3:**
>
> ```
> Input: [7,6,4,3,1]
> Output: 0
> Explanation: In this case, no transaction is done, i.e. max profit = 0.
> ```

## Solution using iterators

```cpp
// 05/04/2020
int maxProfit(vector<int>& prices) {
    if (prices.empty())
        return 0;
    int profit = 0;
    for(auto it = prices.cbegin(); it != prices.cend() -1; ++it){
        int delta = *(it+1) - *it;
        profit += delta>0?delta:0;
    }
    return profit;
}
```
## Solution using indices

```cpp
// 05/04/2020
int maxProfit(vector<int>& prices) {
    if(prices.size()<2) return 0;
    int profit = 0;
    for(int i = 1; i < prices.size(); ++i){
        int delta = prices[i] - prices[i-1];
        profit += delta>0?delta:0;
    }
    return profit;
}
```
## Using `std::accumulate`

```cpp
// 27/06/2020
int maxProfit(vector<int>& prices) {
    if(prices.size()<2) return 0;
    int prev = prices[0];
    return accumulate(prices.begin()+1, prices.end(), 0,
        [&prev](int a, int b){int d = b - prev; prev=b; return a+(d>0?d:0);});
}
```