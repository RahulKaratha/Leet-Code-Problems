class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        new=""
        for i in words[::-1]:
            new+=i
            new+=" "
        return new.rstrip(" ")       
