class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<=1:
            return 0
        else:
            nums.sort()
            max=0
            for i in range(len(nums)-1):
                if (nums[i+1]-nums[i])>max:
                   max=nums[i+1]-nums[i]
            return max
        