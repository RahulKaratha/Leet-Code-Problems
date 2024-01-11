class Solution(object):
    def truncateSentence(self, s, k):
      s=s.split()
      ret=""
      for i in range(k):
          ret+=s[i]+" "

      return ret.rstrip(" ")