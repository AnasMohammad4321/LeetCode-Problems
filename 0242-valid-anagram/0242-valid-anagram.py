class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) == len(t)):
            mydict = {}
            for char in s:
                if (char in mydict):
                    mydict[char] += 1
                else:
                    mydict[char] = 1
            
            for char in t:
                if (char in mydict):
                    mydict[char] -= 1
                else:
                    return False
            for key in mydict.keys():
                if (mydict[key] != 0):
                    return False
            return True

                    

            
        