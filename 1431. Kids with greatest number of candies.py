class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
         ret=[]
         great=0
         for j in candies:
             if j>great:
                 great=j
         for i in candies:
             if i+extraCandies>=great:
                  ret.append(True)
             else:
                 ret.append(False)
         return ret