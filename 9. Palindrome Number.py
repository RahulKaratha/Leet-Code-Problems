
#Given an integer x, return true if x is a palindrome, and false otherwise

class Solution(object):
    def isPalindrome(self,x):
        if str(x)==str(x)[::-1]:
           return True
        else:
            return False
