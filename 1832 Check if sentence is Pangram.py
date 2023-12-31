class Solution(object):
    def checkIfPangram(self, sentence):
        v=0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i not in sentence:
                return False
                v=1
        if v==0:
            return True