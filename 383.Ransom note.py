class Solution(object):
    def canConstruct(self, ransomNote, magazine):
             D={}
             for i in magazine:
                 D[i]=0
             for j in magazine:
                 D[j]+=1
             d={}
             for k in ransomNote:
                 d[k]=0
             for l in ransomNote:
                 d[l]+=1
             bool=True
             for word in ransomNote:
                 if word not in magazine:
                     bool=False
                     break
                 if d[word]>D[word]:
                     bool= False 
                     break
             return bool

        
