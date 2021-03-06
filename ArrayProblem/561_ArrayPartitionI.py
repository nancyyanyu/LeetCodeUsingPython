#561. Array Partition I
#https://leetcode.com/problems/array-partition-i/discuss/

'''Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.'''

#my solution
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortlist=sorted(nums)
        res=0
        for i in range(len(nums)/2):
            res=res+sortlist[i*2]
        return res

#smarter solution-one line answer 
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(nums.sort()[::2])
    
#smarter solution
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sum=0
        for i in range(len(nums)):
            if i%2==0:
                sum+=nums[i]
        return sum
    
'''Thought: every other number starting from the second largest number is adopted.'''





