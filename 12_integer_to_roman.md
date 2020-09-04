# 12 - Integer to Roman

[leetcode link](https://leetcode.com/problems/integer-to-roman/)

> ...Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

😱😱😱

```cpp
class Solution {
public:
    static char* array = ["I", "II", "III"];
    
    string intToRoman(int num, int n = 0) {
        auto symbols = vector<char>{'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        int x = num%10;
        std::string str_x;
        switch(x)
        {
        case 0:
            break;
        case 1:
        case 2:
        case 3:
            for (int i = 0; i < x; i++)
                str_x += symbols[n*2];
            break;
        case 4:
            str_x += symbols[n*2];
            str_x += symbols[n*2+1];
            break;
        case 5:
            str_x += symbols[n*2+1];
            break;
        case 6:
        case 7:
        case 8:
            str_x += symbols[n*2+1];
            for (int i = 5; i < x; i++)
                str_x += symbols[n*2];
            break;
        case 9:
            str_x += symbols[n*2];
            str_x += symbols[n*2+2];
            break;
        }
        if (num >= 10)
            return intToRoman(num/10, n+1) + str_x;
        return str_x;
    }
};
```