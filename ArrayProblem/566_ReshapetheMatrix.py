#566. Reshape the Matrix
#https://leetcode.com/problems/reshape-the-matrix/description/

'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
'''

#my solution
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        product=len(nums)*len(nums[0])
        if r*c!=product:
            res=nums
        else:
            l=[]
            for i in nums:
                for j in i:
                    l.append(j)
            res=[]
            count=-1
            for k in range(r):
                res.append([])
                for t in range(c):
                    count+=1
                    res[k].append(l[count])
        return res
        
#smarter solution


'''Thought: .'''
