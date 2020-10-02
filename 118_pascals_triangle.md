# 118 - Pascal's Triangle

[leetcode link](https://leetcode.com/problems/pascals-triangle/)

> Given a non-negative integer *numRows*, generate the first *numRows* of Pascal's triangle.
>
> ![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
>  In Pascal's triangle, each number is the sum of the two numbers directly above it.
>
> **Example:**
>
> ```
> Input: 5
> Output:
> [
>      [1],
>     [1,1],
>    [1,2,1],
>   [1,3,3,1],
>  [1,4,6,4,1]
> ]
> ```

## Recursive solution

```cpp
// 08/03/2020
vector<vector<int>> generate(int numRows) {
    if(numRows == 0)
        return vector<vector<int>>();
    if(numRows == 1)
        return vector<vector<int>>{{1}};
    auto res = generate(numRows-1);
    res.push_back(generate_line(res.back()));
    return res;
}

vector<int> generate_line(const vector<int>& line){
    vector<int> v(line.size()+1);
    v[0] = 1;
    v[line.size()] = 1;
    for (int i = 0; i<line.size()-1; i++){
        v[1+i] = line[i] + line[i+1];
    }
    return v;
}
```