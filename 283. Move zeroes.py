class Solution(object):
    def moveZeroes(self, nums):
        count=[]
        for i in nums:
             if i==0:
                 count.append(0)
        
        for i in range(len(count)):
            nums.remove(0)
        nums+=count