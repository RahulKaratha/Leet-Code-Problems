class Solution(object):
    def isUgly(self, n):
        ugly=True
        if n==1:
            return ugly
        if n==0:
            return ugly
        if n<0:
            n=-n
        if n>1:
          while True:
            print("\n",n)
            if n%5==0:
                n/=5
            elif n%3==0:
                print(n)
                n/=3
                print(n)
            elif n%2==0:
                n/=2  
            elif n==1:
                break
            else:
    
                ugly=False
                break
          return ugly
        