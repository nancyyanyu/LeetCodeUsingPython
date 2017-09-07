#442. Find All Duplicates in an Array
#https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

'''Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?'''

#my solution
#

#smarter solution-one line answer 
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for x in nums:
            if nums[abs(x)-1]<0:
                res.append(abs(x))
            else:
                nums[abs(x)-1]*=-1
        return res


'''Thought: 所有元素都在1~len(nums)之间，所以所有元素减一都可以对应到nums的某个index上。
遍历每个元素，其减一作为index标记对应元素负号，由于所有元素都是正的，对应到的元素如果是负的，说明之前标记过，
即本元素是重复的，则append到结果中'''
