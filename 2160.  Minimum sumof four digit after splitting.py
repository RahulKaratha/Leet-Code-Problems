class Solution(object):
    def minimumSum(self, num):
        num=str(num)
        num=list(num)
        num.sort()
        num1=int(num[0]+num[3])
        num2=int(num[1]+num[2])
        return num1+num2