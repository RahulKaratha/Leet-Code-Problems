class Solution(object):
    def subtractProductAndSum(self, n):
         n=str(n)
         a=1
         b=0
         for i in n:
             a*=int(i)
             b+=int(i)
        
         return a-b