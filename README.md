# LeetCodeUsingPython
LeetCode practice using python language

[python learning note](https://github.com/nancyyanyu/LeetCodeUsingPython/blob/master/PythonLearning.md)

## Problem List
* #001. Two Sum
* #004. Median of Two Sorted Arrays
* #015. 3Sum
* #016. 3Sum Closest
* #018. 4Sum
* #026. Remove Duplicates from Sorted Array
* #027. Remove Element
* #0
* #035. Search Insert Position

* #039. Combination Sum
* #041. First Missing Positive


* #055. Jump Game
* #442. Find All Duplicates in an Array
* #485. Max Consecutive Ones
* #561. Array Partition I
* #566. Reshape the Matrix
* #667. Beautiful Arrangement II
* #766. Toeplitz Matrix


## Array
### 561. Array Partition I
**LeetCode link:** https://leetcode.com/problems/array-partition-i/description/

**Problem description:**

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

**Thought:** 

every other number starting from the second largest number is adopted.

-----------------------------

### 566. Reshape the Matrix
**LeetCode link:** https://leetcode.com/problems/reshape-the-matrix/description/

**Thought:** 

1. sum(,[])
2. zip(*([iter(flat)]*c))
3. 运行到return直接结束

-----------------------------


### 442. Find All Duplicates in an Array
**LeetCode link:** https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

**Thought:** 

所有元素都在1~len(nums)之间，所以所有元素减一都可以对应到nums的某个index上。
遍历每个元素，其减一作为index标记对应元素负号，由于所有元素都是正的，对应到的元素如果是负的，说明之前标记过，
即本元素是重复的，则append到结果中

-----------------------------

###  485. Max Consecutive Ones
**LeetCode link:** https://leetcode.com/problems/max-consecutive-ones/description/

**Thought:** 

My answer is to change the original list and don't forget to refer the former index. Other solution renews the maximum number 
every iteration.

-----------------------------

###  667. Beautiful Arrangement II
**LeetCode link:** https://leetcode.com/problems/beautiful-arrangement-ii/description/

**Thought:** 

Thought: When k = n-1, a valid construction is [1, n, 2, n-1, 3, n-2, ....]. 
One way to see this is, we need to have a difference of n-1, which means we need 1 and n adjacent; 
then, we need a difference of n-2, etc.

This leads to the following idea: we will put [1, 2, ...., n-k-1] first, 
and then we have N = k+1 adjacent numbers left, of which we want k different differences. 
This is just the answer above translated by n-k-1: we'll put [n-k, n, n-k+1, n-1, ....] after

-----------------------------

###  027. Remove Element
**LeetCode link:** https://leetcode.com/problems/remove-element/description/

**Thought:** 

我的做法是利用了语言特性。但不如第二个参考答案用的好。首先remove(int)按照顺序删去指定int，count(obj)可以得出list中obj的个数。
参考答案一更机智。通过设定起始index，在遇到val时把当下数字和end对换，start点不变，end点前移，leave a 'val' behind.不遇到val则start点前移，
直到end超过start时取nums中前start个数字

-----------------------------

###  039. Combination Sum
**LeetCode link:** https://leetcode.com/problems/combination-sum/description/

**Thought:** 

-----------------------------

###  766. Toeplitz Matrix
**LeetCode link:** https://leetcode.com/problems/toeplitz-matrix/description/ 

**Thought:** 

Think really carefully about the relationship between i and j.

-----------------------------

###  001. Two Sum
**LeetCode link:** https://leetcode.com/problems/two-sum/description/

**Thought:** 

-----------------------------

###  004. Median of Two Sorted Arrays
**LeetCode link:** https://leetcode.com/problems/median-of-two-sorted-arrays/description/

**Thought: **

hard.
Use binary search.
Note the median is used for dividing a set into two equal length subsets, that one subset is always greater than the other

-----------------------------

###  015. 3Sum
**LeetCode link:** https://leetcode.com/problems/3sum/description/

**Thought:** carefully deal with duplicate; use 'left' and 'right' index to narrow the inner loop.

-----------------------------

###  016. 3Sum Closest
**LeetCode link:** https://leetcode.com/problems/3sum-closest/description/

**Thought:** same idea as 015. 3Sum, left and right index is a useful way to reduce time from N^3 to N^2

-----------------------------

###  018. 4Sum
**LeetCode link:** https://leetcode.com/problems/4sum/description/

**Thought:** pass

-----------------------------

###  026. Remove Duplicates from Sorted Array

**LeetCode link:** 
**Thought:** pass

-----------------------------

###  55. Jump Game
**LeetCode link:** https://leetcode.com/problems/jump-game/description/

**Thought:** 当碰到0的时候判断现在的maximum jump是否大于尾数，maximum jump想象成汽油，你能驶过的距离是现在已经驶过的距离加上这一站的汽油量nums[i]，记录行程中这个汽油量的最大值。

-----------------------------

###  35. Search Insert Position
**LeetCode link:** https://leetcode.com/problems/search-insert-position/description/

**Thought:** easy

-----------------------------

###  41. First Missing Positive
**LeetCode link:** https://leetcode.com/problems/first-missing-positive/description/

**Thought:** 好好使用set的功能

-----------------------------

###  
**LeetCode link:** 

**Thought:** 

-----------------------------

###  
**LeetCode link:** 

**Thought:** 
