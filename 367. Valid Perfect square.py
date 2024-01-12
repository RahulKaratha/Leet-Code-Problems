class Solution(object):
    def isPerfectSquare(self, num):
        n=num**0.5
        if int(n)==n:
            return True
        else:
            return False