class Solution(object):
    def isPowerOfFour(self, n):
        while True:
                if n==1:
                    return True
                    break
                elif n%4!=0 or n==0:
                    return False
                    break
                n/=4
        