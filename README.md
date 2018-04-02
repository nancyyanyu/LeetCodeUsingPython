# LeetCodeUsingPython
LeetCode practice using python language

[python learning note](https://github.com/nancyyanyu/LeetCodeUsingPython/blob/master/PythonLearning.md)

## Problem List
* #001. Two Sum
* #561. Array Partition I
* #566. Reshape the Matrix
* #442. Find All Duplicates in an Array
* #485. Max Consecutive Ones
* #667. Beautiful Arrangement II
* #027. Remove Element
* #039. Combination Sum
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

**Thought:** 

所有元素都在1~len(nums)之间，所以所有元素减一都可以对应到nums的某个index上。
遍历每个元素，其减一作为index标记对应元素负号，由于所有元素都是正的，对应到的元素如果是负的，说明之前标记过，
即本元素是重复的，则append到结果中

-----------------------------


###  485. Max Consecutive Ones
**LeetCode link:** https://leetcode.com/problems/max-consecutive-ones/description/

**Problem description:**

Given a binary array, find the maximum number of consecutive 1s in this array.

**Thought:** 

My answer is to change the original list and don't forget to refer the former index. Other solution renews the maximum number 
every iteration.

-----------------------------


###  667. Beautiful Arrangement II
**LeetCode link:** https://leetcode.com/problems/beautiful-arrangement-ii/description/

**Problem description:**

Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

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

**Problem description:**

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

**Thought:** 

我的做法是利用了语言特性。但不如第二个参考答案用的好。首先remove(int)按照顺序删去指定int，count(obj)可以得出list中obj的个数。
参考答案一更机智。通过设定起始index，在遇到val时把当下数字和end对换，start点不变，end点前移，leave a 'val' behind.不遇到val则start点前移，
直到end超过start时取nums中前start个数字

-----------------------------


###  039. Combination Sum
**LeetCode link:** https://leetcode.com/problems/combination-sum/description/

**Problem description:**

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

**Thought:** 


-----------------------------


###  766. Toeplitz Matrix
**LeetCode link:** https://leetcode.com/problems/toeplitz-matrix/description/ 

**Problem description:**

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 
**Thought:** 

Think really carefully about the relationship between i and j.

-----------------------------


###  001. Two Sum
**LeetCode link:** https://leetcode.com/problems/two-sum/description/

**Problem description:**

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


**Thought:** 

-----------------------------


###  
**LeetCode link:** 

**Problem description:**

**Thought:** 

-----------------------------


###  
**LeetCode link:** 

**Problem description:**

**Thought:** 

-----------------------------


###  
**LeetCode link:** 

**Problem description:**

**Thought:** 

-----------------------------


###  
**LeetCode link:** 

**Problem description:**

**Thought:** 

-----------------------------


###  
**LeetCode link:** 

**Problem description:**

**Thought:** 

-----------------------------


###  
**LeetCode link:** 

**Problem description:**

**Thought:** 
