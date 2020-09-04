# 7 - Reverse Integer

[leetcode link](https://leetcode.com/problems/reverse-integer/)

> Given a 32-bit signed integer, reverse digits of an integer.

## working on the integer digits - O(nb digits)

```cpp
int reverse(int x) {
    int r = 0;
    while (x) {
        try {
            r = r * 10 + x % 10;
        } catch (...) {
            return 0;
        }
        x /= 10;
    }
    return r;
}
```

## convert to string, reverse, convert back to integer - O(nb digits)

```cpp
int reverse(int x) {
    auto s = to_string(x);
    auto begin = s[0] == '-'? s.begin()+1: s.begin();
    std::reverse(begin, s.end());
    try {
        return std::stoi(s);
    }
    catch(std::out_of_range& e) {
        return 0;
    }
}
```
