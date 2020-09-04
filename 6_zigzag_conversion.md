# 6 - ZigZag Conversion

[leetcode link](https://leetcode.com/problems/zigzag-conversion/)

> The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
> 
> ```
> P   A   H   N
> A P L S I I G
> Y   I   R
> ```
> And then read line by line: `"PAHNAPLSIIGYIR"`
> 
> Write the code that will take a string and make this conversion given a number of rows:

**TODO:** Rework that solution.

```cpp
string convert(string s, int numRows) {
    if (numRows == 1 or s.size()<2)
        return s;
    int nb_col = s.size() / 2 +1;
    auto matrix = vector<vector<char>>(
        numRows, 
        vector<char>(nb_col, ' ')
    );
    //cout << nb_col << " x " << numRows << "\n";
    int i = 0;
    int x = 0;
    int y = 0;
    for(auto c : s){
        //cout << x <<", " << y << " -> " <<c << "\n";
        matrix[y][x] = c;
        if ( i < numRows-1 ){
            y++;
            i++;
        }
        else if (i < 2*numRows-2-1){
            x++;
            y--;
            i++;
        }
        else{
            x++;
            i = 0;
            y = 0;
        }
    }
    string ret;
    for (const auto& line : matrix){
        for (const auto &c: line){
            //cout << c;
            if (c != ' ')
                ret += c;
        }
        //cout << "]\n";
    }
    return ret;
}
```
