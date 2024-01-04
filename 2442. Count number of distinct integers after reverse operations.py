class Solution(object):
    def countDistinctIntegers(self, nums):
         rev=[]
         for i in nums:
             i=str(i)
             i=i[::-1]
             i=int(i)
             rev.append(i)
         nums+=rev
         return len(set(nums))