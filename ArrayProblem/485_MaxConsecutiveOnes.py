#485. Max Consecutive Ones
#https://leetcode.com/problems/max-consecutive-ones/description/

'''Given a binary array, find the maximum number of consecutive 1s in this array.'''

#my solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums))[1:]:
            if nums[i]>0 and nums[i-1]>0:
                nums[i]=nums[i-1]+1
        return max(nums)

#other solution 
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans


'''Thought: My answer is to change the original list and don't forget to refer the former index. Other solution renews the maximum number 
every iteration.'''
