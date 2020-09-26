# 374 - Guess Number Higher or Lower

[leetcode link](https://leetcode.com/problems/guess-number-higher-or-lower/)

> We are playing the Guess Game. The game is as follows:
>
> I pick a number from **1** to ***n\***. You have to guess which number I picked.
>
> Every time you guess wrong, I'll tell you whether the number is higher or lower.
>
> You call a pre-defined API `guess(int num)` which returns 3 possible results (`-1`, `1`, or `0`):
>
> ```
> -1 : My number is lower
>  1 : My number is higher
>  0 : Congrats! You got it!
> ```
>
> **Example :**
>
> ```
> Input: n = 10, pick = 6
> Output: 6
> ```

## Solution: binary search

```cpp
int guessNumber(int n) {
    int l = 0, r = n;
    while(l<=r){
        int mid = l + (r-l)/2;
        if(int g = guess(mid); g == 1)
            l = mid+1;
        else if(g == -1)
            r = mid-1;
        else
            return mid;
    }
    return -1;
}
```