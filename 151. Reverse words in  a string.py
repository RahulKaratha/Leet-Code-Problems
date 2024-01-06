class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        new=""
        for i in words[::-1]:
            new+=i
            new+=" "
        return new.rstrip(" ")       
    
''' Runtime 4 ms
Beats 99.59%
Memory 13.8 MB
Beats 27.87%'''