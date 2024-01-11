class Solution(object):
    def differenceOfSum(self, nums):
        Sum=sum(nums)
        digit=0
        for i in nums:
            i=str(i)
            for j in i:
                digit+=int(j)
        return Sum-digit