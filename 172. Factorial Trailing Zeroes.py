class Solution(object):
    def trailingZeroes(self, n):
        f=1
        for i in range(1,n+1):
            f*=i

        f=str(f)
        trailing=0

        for j in f[::-1]:
            if j=="0":
                trailing+=1
            else:
                break
        return trailing 