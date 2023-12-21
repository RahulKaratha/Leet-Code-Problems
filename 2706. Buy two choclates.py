class Solution(object):
    def buyChoco(self, prices, money):
        cost=prices[0]+prices[1]
        for i in prices:
            n=prices.index(i)
            for j in prices[n::]:
                if i+j<cost:
                    cost=i+j

        if money-cost>0:
            return money-cost
        else:
            return money