class Solution(object):
    def findWordsContaining(self, words, x):
        i=0
        ret=[]
        for ele in words:
            if x in ele:
                ret.append(i)
                i+=1
            else:
                i+=1
        return ret

        