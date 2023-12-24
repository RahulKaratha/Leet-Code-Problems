class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for ele in operations:
            if "+" in ele:
                x+=1
            if "-" in ele:
                x-=1
        return x
