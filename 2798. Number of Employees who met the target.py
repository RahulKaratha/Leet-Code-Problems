class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        work=0
        for emp in hours:
            if emp>=target:
                work+=1

        return work