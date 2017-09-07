#027. Remove Element
#https://leetcode.com/problems/remove-element/description/

'''Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.'''

#my solution
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while(i<=(len(nums)-1)):
            if nums[i]==val:
                nums.remove(nums[i])
                i-=1
            i+=1
        return len(nums)

#smarter solution
class Solution(object):
  def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        nums[:] = nums[:start]
        return start

#smarter solution with .remove()
class Solution(object):
    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
            

'''Thought:我的做法是利用了语言特性。但不如第二个参考答案用的好。首先remove(int)按照顺序删去指定int，count(obj)可以得出list中obj的个数。
参考答案一更机智。通过设定起始index，在遇到val时把当下数字和end对换，start点不变，end点前移，leave a 'val' behind.不遇到val则start点前移，
直到end超过start时取nums中前start个数字 '''
