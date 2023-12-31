class Solution(object):
    def mostWordsFound(self, sentences):
       max=0
       for ele in sentences:
           words=ele.split()
           if len(words)>max:
               max=len(words)
       return max