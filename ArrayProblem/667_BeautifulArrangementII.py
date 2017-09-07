#667. Beautiful Arrangement II
#

'''Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.'''

#my solution
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res=range(1,n-k)
        for i in range(k+1):
            if i%2==0:
                res.append(n-k+i/2)
            else:
                res.append(n-i/2)
        return res

#smarter solution



'''Thought: When k = n-1, a valid construction is [1, n, 2, n-1, 3, n-2, ....]. 
One way to see this is, we need to have a difference of n-1, which means we need 1 and n adjacent; 
then, we need a difference of n-2, etc.

This leads to the following idea: we will put [1, 2, ...., n-k-1] first, 
and then we have N = k+1 adjacent numbers left, of which we want k different differences. 
This is just the answer above translated by n-k-1: we'll put [n-k, n, n-k+1, n-1, ....] after.
重点是想到k = n-1, a valid construction is [1, n, 2, n-1, 3, n-2, ....]，然后拓展至N=k+1
'''
