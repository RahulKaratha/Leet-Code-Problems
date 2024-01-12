class Solution(object):
    def reverseVowels(self, s):
        vow=[]
        for i in s:
            if i in "aeiouAEIOU":
                vow.append(i)
        vow.reverse()
        S=""
        count=0
        for j in s:
            if j not in "aeiouAEIOU":
                S+=j
            if j in "aeiouAEIOU":
                S+=vow[count]
                count+=1
        return S