class Solution(object):
    def majorityElement(self, nums):
         sets=set(nums)
         d=[0,0]
         for i in sets:
             count=0
             for j in nums:
                 if i==j:
                     count+=1
             if count>d[1]:
                 d=[i,count]
         return d[0]
        