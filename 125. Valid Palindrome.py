class Solution(object):
    def isPalindrome(self, s):
        test=""
        for i in s:
            if i.isalnum():
                test+=i
        
        test=test.lower()
        if test==test[::-1]:
            return True
        else: 
            return False
        