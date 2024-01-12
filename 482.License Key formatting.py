class Solution(object):
    def licenseKeyFormatting(self, s, k):
        license=""
        count=0
        for i in s[::-1].upper():
            if count==k:
                license+="-"
                count=0
            if i.isalnum():
                license+=i
                count+=1
        return license[::-1].lstrip("-")