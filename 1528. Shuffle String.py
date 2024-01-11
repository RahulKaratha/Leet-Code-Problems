class Solution(object):
    def restoreString(self, s, indices):
        word=[]
        for m in range(len(s)):
           word.append("x")
        count=0
        for i in s: 
            word[indices[count]]=i
            count+=1
        ret=""
        for n in word:
            ret+=n
        return ret