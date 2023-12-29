class Solution(object):
    def smallestEvenMultiple(self, n):
        if n%2!=0:
            return n+n
        else:
            return n
        