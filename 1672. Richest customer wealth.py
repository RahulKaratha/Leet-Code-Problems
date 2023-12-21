class Solution(object):
    def maximumWealth(self, accounts):
        rich=0
        for acc in accounts:
            wealth=sum(acc)
            if wealth>rich:
                rich=wealth
        return rich