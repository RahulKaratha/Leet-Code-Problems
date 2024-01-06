class Solution(object):
    def isPowerOfTwo(self, n):
            while True:
                if n==1:
                    return True
                    break
                elif n%2!=0 or n==0:
                    return False
                    break
                n/=2
                