class Solution(object):
    def sumOfMultiples(self, n):
       count=0
       for i in range(1,n+1):
           if i%5==0 or i%3==0 or i%7==0:
               count+=i
       return count