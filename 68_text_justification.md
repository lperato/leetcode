# 68 - Text Justification

[leetcode link](https://leetcode.com/problems/text-justification/)

> Given an array of words and a width *maxWidth*, format the text such that each line has exactly *maxWidth* characters and is fully (left and right) justified.
>
> You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly *maxWidth* characters.
>
> Extra spaces between words should be distributed as evenly as  possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than  the slots on the right.
>
> For the last line of text, it should be left justified and no **extra** space is inserted between words.
>
> **Note:**
>
> - A word is defined as a character sequence consisting of non-space characters only.
> - Each word's length is guaranteed to be greater than 0 and not exceed *maxWidth*.
> - The input array `words` contains at least one word.
>
> **Example 1:**
>
> ```
> Input:
> words = ["This", "is", "an", "example", "of", "text", "justification."]
> maxWidth = 16
> Output:
> [
>    "This    is    an",
>    "example  of text",
>    "justification.  "
> ]
> ```
>
> **Example 2:**
>
> ```
> Input:
> words = ["What","must","be","acknowledgment","shall","be"]
> maxWidth = 16
> Output:
> [
>   "What   must   be",
>   "acknowledgment  ",
>   "shall be        "
> ]
> Explanation: Note that the last line is "shall be    " instead of "shall     be",
>              because the last line must be left-justified instead of fully-justified.
>              Note that the second line is also left-justified becase it contains only one word.
> ```
>
> **Example 3:**
>
> ```
> Input:
> words = ["Science","is","what","we","understand","well","enough","to","explain",
>          "to","a","computer.","Art","is","everything","else","we","do"]
> maxWidth = 20
> Output:
> [
>   "Science  is  what we",
>   "understand      well",
>   "enough to explain to",
>   "a  computer.  Art is",
>   "everything  else  we",
>   "do                  "
> ]
> ```

## Solution

```cpp
// 13/03/2020
vector<string> fullJustify(vector<string>& words, int maxWidth) {
    vector<string> res;
    int line_size=0;
    auto it = words.begin();
    auto start = it;
    for(; it != words.end(); it++){
        int space = (it==start)?0:1;
        if(line_size + space + it->size() > maxWidth){
            res.emplace_back(make_justified_line(start, it, maxWidth, line_size));
            start = it;
            line_size = it->size();
        }else{
            line_size += space + it->size();
        }
    }
    res.emplace_back(make_left_aligned_line(start, words.end(), maxWidth));
    return res;
}

string make_left_aligned_line(vector<string>::const_iterator begin, vector<string>::const_iterator end, int max_width){
    string s(*begin);
    for (auto it = begin+1; it != end; ++it){
        s.append(1, ' ');
        s += *it;
    }
    s.append(max_width-s.size(), ' ');
    return move(s);
}

string make_justified_line(vector<string>::const_iterator begin, vector<string>::const_iterator end, int max_width, int line_size){
    int nb_words = end - begin; 
    string res(*begin);
    if(nb_words == 1){
        return make_left_aligned_line(begin, end, max_width);
    }  
    int total_space_size = max_width - (line_size - (nb_words-1));
    int space_size = max(1, total_space_size / (nb_words-1));
    int additional_space = total_space_size - space_size * (nb_words-1);
    for(auto it = begin+1; it != end; ++it){
        int add_space = 0;
        if(additional_space>0){
            additional_space--;
            add_space = 1;
        }
        res.append(space_size + add_space, ' ');
        res += *it;
    }
    return move(res);    
}
```
