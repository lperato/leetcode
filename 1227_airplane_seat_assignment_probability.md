# 1227 - Airplane Seat Assignment Probability

[leetcode link](https://leetcode.com/problems/airplane-seat-assignment-probability/)

> `n` passengers board an airplane with exactly `n` seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:
>
> - Take their own seat if it is still available, 
> - Pick other seats randomly when they find their seat occupied 
>
> What is the probability that the n-th person can get his own seat?
>
> **Example 1:**
>
> ```
> Input: n = 1
> Output: 1.00000
> Explanation: The first person can only get the first seat.
> ```
>
> **Example 2:**
>
> ```
> Input: n = 2
> Output: 0.50000
> Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).
> ```

## Solution 1: Don't think, recurse! - O(n)

```cpp
// 14/09/2020
double nthPersonGetsNthSeat(int n) {
    if(n == 1) return 1;
    return 1.0/(double)n + nthPersonGetsNthSeat(n-1) * (double)(n-2)/(double)n;
}
```
## Solution 2: Think, don't code! - O(1)

```cpp
// 14/09/2020
double nthPersonGetsNthSeat(int n) {
    return (n == 1)?1.0:0.5;
}
```

