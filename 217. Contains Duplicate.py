class Solution(object):
    def containsDuplicate(self, nums):
      if len(set(nums))!=len(nums):
          return True
      else:
           return False
        