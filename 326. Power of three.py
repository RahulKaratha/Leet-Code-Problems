class Solution(object):
    def isPowerOfThree(self, n):
       while True:
                if n==1:
                    return True
                    break
                elif n%3!=0 or n==0:
                    return False
                    break
                n/=3