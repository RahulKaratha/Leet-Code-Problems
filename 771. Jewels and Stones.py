class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        num=0
        for j in jewels:
            num+=stones.count(j)
        return num 
