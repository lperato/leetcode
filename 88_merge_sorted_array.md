# 88 - Merge Sorted Array

[leetcode link](https://leetcode.com/problems/merge-sorted-array/)

> Given two sorted integer arrays *nums1* and *nums2*, merge *nums2* into *nums1* as one sorted array.
>
> **Note:**
>
> - The number of elements initialized in *nums1* and *nums2* are *m* and *n* respectively.
> - You may assume that *nums1* has enough space (size that is **equal** to *m* + *n*) to hold additional elements from *nums2*.
>
> **Example:**
>
> ```
> Input:
> nums1 = [1,2,3,0,0,0], m = 3
> nums2 = [2,5,6],       n = 3
> 
> Output: [1,2,2,3,5,6]
> ```
>
> **Constraints:**
>
> - `-10^9 <= nums1[i], nums2[i] <= 10^9`
> - `nums1.length == m + n`
> - `nums2.length == n`

## Solution 1 : 2 +1 pointers

```cpp
// 08/08/2020 - 2 +1 pointers
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    for(int i = m-1, j = n-1, k = m+n-1; k>=0;){
        if(i>=0 && (j < 0 || nums1[i] > nums2[j])) nums1[k--] = nums1[i--];
        else nums1[k--] = nums2[j--];
    }
}
```
### Shorter version

```cpp
// 08/08/2020 - 2 +1 pointers - shorter version
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    for(int i = m-1, j = n-1, k = m+n-1; k>=0;)
        nums1[k--] = (i>=0 && (j < 0 || nums1[i] > nums2[j]))?nums1[i--]:nums2[j--];
} 
```
## [Bad] Solution 2: no idea!

```cpp
// 03/13/2020 - I dont understand what I was doing! :-)
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    if (n == 0 || nums2.empty())
        return;
    int j = 0;
    for(int i = 0; i < nums1.size(); i++){
        if (i<m){
            if(nums2[0]<nums1[i]){
                swap(nums2[0], nums1[i]);
                for(int k = 0;k<n-1;++k){
                    if(nums2[k]>nums2[k+1])
                        swap(nums2[k], nums2[k+1]);
                }
            }
        }else{
            nums1[i] = nums2[j++];   
        }
    }
}
```