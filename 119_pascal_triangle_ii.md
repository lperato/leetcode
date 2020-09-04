#  119 - Pascal's Triangle II

[leetcode link](https://leetcode.com/problems/pascals-triangle-ii/)

> Given an integer `rowIndex`, return the `rowIndexth` row of the Pascal's triangle.
>
> Notice that the row index starts from **0**.

## Recursive solution

### Naïve

```cpp
// recursive version
vector<int> getRow(int rowIndex){
    if(rowIndex == 0) return {1};
    auto row = getRow(rowIndex -1);
    vector<int> result(row.size()+1);
    for(int i=0, s = result.size(); i != s; ++i)
        result[i] = (i!=0?row[i-1]:0) + (i!=s-1?row[i]:0);
    return result;
}
```
### Working directly on result of previous level

```cpp
// recursive version taking less space
vector<int> getRow(int rowIndex){
    if(rowIndex == 0) return {1};
    auto row = getRow(rowIndex -1);
    for(int i = row.size()-1; i >=0; --i)
        row[i] += (i!=0?row[i-1]:0);
    row.push_back(1);
    return row;
}
```
## Iterative solution

```cpp
vector<int> getRow(int rowIndex) {
    if(rowIndex==0) return {1};
    vector<int> rows{1,1};
    for (int i = 1; i < rowIndex; i++){
        next_row(rows);
    }
    return rows;
}

void next_row(vector<int>& rows){
    int prev = 1;
    for(int i=1; i < rows.size(); i++){
        int tmp = prev;
        prev = rows[i];
        rows[i] += tmp;
    }
    rows.push_back(1);
}
```