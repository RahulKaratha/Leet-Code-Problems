class Solution(object):
    def defangIPaddr(self, address):
        defanged=""
        for i in address:
            if not i.isdecimal():
                defanged+="[.]"
            else:
                defanged+=i
        return defanged