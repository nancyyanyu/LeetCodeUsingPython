# LeetCodeUsingPython
LeetCode practice using python language
## List
* #561. Array Partition I
* #566. Reshape the Matrix
* #442. Find All Duplicates in an Array

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

**Problem description:**
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

**Thought:** 
1. sum(,[])
2. zip(*([iter(flat)]*c))
3. 运行到return直接结束

-----------------------------

### 442. Find All Duplicates in an Array
**LeetCode link:** https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

**Problem description:**
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

**Thought:** 所有元素都在1~len(nums)之间，所以所有元素减一都可以对应到nums的某个index上。
遍历每个元素，其减一作为index标记对应元素负号，由于所有元素都是正的，对应到的元素如果是负的，说明之前标记过，
即本元素是重复的，则append到结果中

-----------------------------

### .
**LeetCode link:** 

**Problem description:**
