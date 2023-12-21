class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            test=haystack.split(needle)
            if needle==test[0]:
                return 0

            else:
                return len(test[0])
        else:
            return -1
        