class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result = 0
        prev = 0
        for i in range(len(s)):
            current = s[i]
            if (prev < mydict[current]):
                result += mydict[current] - 2*prev
            else:
                result += mydict[current]
                
            prev = mydict[current]
        return result
        