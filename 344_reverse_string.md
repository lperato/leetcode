# 344 - Reverse String

[leetcode link](https://leetcode.com/problems/reverse-string/)


> Write a function that reverses a string. The input string is given as an array of characters char[].

> Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


## The obvious STL way

```cpp
void reverseString(vector<char>& s){
    reverse(s.begin(), s.end());
}
```

## Recursive version

```cpp
void reverseString(vector<char>& s, int pos = 0){
    auto sz = s.size();
    if(pos>= sz/2) return;
    swap(s[pos], s[sz-1-pos]);
    reverseString(s, pos+1);
}
```

## Two pointers - using indices ([] operator)

### Long and ugly (manual swap)

```cpp
void reverseString(vector<char>& s){
    for(int i = 0, j = s.size()-1; i < j; ++i, --j){
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}
```

### Shorter (using std::swap)

```cpp
void reverseString(vector<char>& s){
    for(int i = 0, j = s.size()-1; i < j; ++i, --j)
        swap(s[i], s[j]);
}
```

### One liner

```cpp
void reverseString(vector<char>& s){
    for(int i = 0, j = s.size()-1; i < j; swap(s[i++], s[j--]));
}
```

## Two pointers - using iterators

### Using std::prev  + iter_swap

```cpp
void reverseString(vector<char>& s){
    if(s.empty())return;    
    for(auto a=s.begin(), b=prev(s.end()); a < b; ++a, --b)
        iter_swap(a, b);
}
```

### Using reverse iteraror + iter_swap
```cpp
void reverseString(vector<char>& s){
    auto a = s.begin();
    auto b = s.rbegin();    
    for(;a < b.base(); ++a, ++b)
        iter_swap(a, b);
}
```

### reverse iterator plus manual swap (ugly)

```cpp
void reverseString(vector<char>& s) {
    auto r = s.rbegin();
    auto i = s.begin();
    while (i < r.base()){
        auto tmp = *i;
        *i = *r;
        *r = tmp;
        i++;
        r++;
    }
}
```

​    



